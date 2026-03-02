from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from db_config.database import get_db
from db_config.models.employee import Employee
from db_config.models.attendance import Attendance
from src.modules.dashboard.schemas import DashboardSummary, AttendanceSummary, EmployeeAttendanceStat
from datetime import date

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/summary", response_model=DashboardSummary)
async def get_dashboard_summary(db: AsyncSession = Depends(get_db)):
    total_employees = (await db.execute(select(func.count(Employee.id)))).scalar()
    today = date.today()
    present_today = (await db.execute(select(func.count(Attendance.id)).filter(Attendance.date == today, Attendance.status == "Present"))).scalar()
    absent_today = (await db.execute(select(func.count(Attendance.id)).filter(Attendance.date == today, Attendance.status == "Absent"))).scalar()

    query = (
        select(Employee.id, Employee.full_name, func.count(Attendance.id).label("present_days"))
        .outerjoin(Attendance, (Attendance.employee_id == Employee.id) & (Attendance.status == "Present"))
        .group_by(Employee.id, Employee.full_name)
    )
    result = await db.execute(query)
    employee_stats = [
        EmployeeAttendanceStat(employee_id=row[0], employee_name=row[1], total_present_days=row[2])
        for row in result.all()
    ]
    
    return DashboardSummary(
        summary=AttendanceSummary(
            total_employees=total_employees,
            present_today=present_today,
            absent_today=absent_today
        ),
        employee_stats=employee_stats
    )
