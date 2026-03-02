from pydantic import BaseModel, EmailStr
from typing import Optional

class EmployeeBase(BaseModel):
    employee_id: str
    full_name: str
    email_address: EmailStr
    department: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        from_attributes = True
