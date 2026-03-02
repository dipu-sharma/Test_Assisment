from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db_config.database import get_db
from db_config.models.attendance import Attendance
from db_config.models.employee import Employee
from src.modules.attendance.schemas import AttendanceCreate, AttendanceResponse
from typing import List, Optional
from datetime import date

router = APIRouter(prefix="/attendance", tags=["Attendance"])

@router.post("/", response_model=AttendanceResponse, status_code=status.HTTP_201_CREATED)
async def mark_attendance(attendance: AttendanceCreate, db: AsyncSession = Depends(get_db)):
    # Verify employee exists
    result = await db.execute(select(Employee).filter(Employee.id == attendance.employee_id))
    employee = result.scalars().first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    if attendance.status not in ["Present", "Absent"]:
         raise HTTPException(status_code=400, detail="Status must be either 'Present' or 'Absent'")

    # Check if attendance already marked for the date
    result = await db.execute(select(Attendance).filter(Attendance.employee_id == attendance.employee_id, Attendance.date == attendance.date))
    existing_attendance = result.scalars().first()
    if existing_attendance:
        # Update existing
        existing_attendance.status = attendance.status
        await db.commit()
        await db.refresh(existing_attendance)
        return existing_attendance
        
    new_attendance = Attendance(**attendance.model_dump())
    db.add(new_attendance)
    await db.commit()
    await db.refresh(new_attendance)
    return new_attendance

@router.get("/{employee_id}", response_model=List[AttendanceResponse])
async def get_employee_attendance(employee_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Attendance).filter(Attendance.employee_id == employee_id).order_by(Attendance.date.desc()))
    return result.scalars().all()

@router.get("/", response_model=List[AttendanceResponse])
async def get_all_attendance(date: Optional[date] = None, db: AsyncSession = Depends(get_db)):
    query = select(Attendance)
    if date:
        query = query.filter(Attendance.date == date)
    result = await db.execute(query.order_by(Attendance.date.desc()))
    return result.scalars().all()
