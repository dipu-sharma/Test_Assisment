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
    allow_origins=[
        "https://test-assisment-98ykor7my-dipu-sharmas-projects.vercel.app",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees_router)
app.include_router(attendance_router)
app.include_router(dashboard_router)


if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8002))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
