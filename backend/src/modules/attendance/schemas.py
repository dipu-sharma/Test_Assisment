from pydantic import BaseModel
from datetime import date
from typing import Optional

class AttendanceBase(BaseModel):
    date: date
    status: str

class AttendanceCreate(AttendanceBase):
    employee_id: int

class AttendanceResponse(AttendanceBase):
    id: int
    employee_id: int

    class Config:
        from_attributes = True
