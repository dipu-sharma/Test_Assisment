from pydantic import BaseModel
from typing import List, Dict

class AttendanceSummary(BaseModel):
    total_employees: int
    present_today: int
    absent_today: int

class EmployeeAttendanceStat(BaseModel):
    employee_id: int
    employee_name: str
    total_present_days: int

class DashboardSummary(BaseModel):
    summary: AttendanceSummary
    employee_stats: List[EmployeeAttendanceStat]
