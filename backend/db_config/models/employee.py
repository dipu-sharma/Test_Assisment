from sqlalchemy import Column, Integer, String
from db_config.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    email_address = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, nullable=False)
