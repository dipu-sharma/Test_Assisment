from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db_config.database import get_db
from db_config.models.employee import Employee
from src.modules.employees.schemas import EmployeeCreate, EmployeeResponse
from typing import List

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
async def create_employee(employee: EmployeeCreate, db: AsyncSession = Depends(get_db)):
    # Check duplicate
    result = await db.execute(select(Employee).filter((Employee.employee_id == employee.employee_id) | (Employee.email_address == employee.email_address)))
    existing_employee = result.scalars().first()
    if existing_employee:
        raise HTTPException(status_code=400, detail="Employee with this ID or Email already exists")
    
    new_employee = Employee(**employee.model_dump())
    db.add(new_employee)
    await db.commit()
    await db.refresh(new_employee)
    return new_employee

@router.get("/", response_model=List[EmployeeResponse])
async def get_employees(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Employee))
    return result.scalars().all()

@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee(employee_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Employee).filter(Employee.id == employee_id))
    employee = result.scalars().first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    await db.delete(employee)
    await db.commit()
    return None
