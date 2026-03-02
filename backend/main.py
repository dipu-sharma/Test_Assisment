from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db_config.database import engine, Base
from db_config.models import *
from src.modules.employees.router import router as employees_router
from src.modules.attendance.router import router as attendance_router
from src.modules.dashboard.router import router as dashboard_router
import contextlib

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="HRMS Lite API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees_router)
app.include_router(attendance_router)
app.include_router(dashboard_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to HRMS Lite API"}
