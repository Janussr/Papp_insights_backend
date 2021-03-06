from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services import parking_overview_service, report_service, parkingarea_service
from app.objects import models

app = FastAPI(title="FastAPI, Docker, and Traefik")

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/report/{id}")
def get_report(id: str, q: Optional[str] = None):
    return report_service.get_report(id)


@app.get("/reports")
def get_reports():
    return report_service.get_all_reports()


@app.get("/parkingareas")
def get_parking_areas():
    return {"parkingareas": parkingarea_service.all_parking_areas()}


@app.get("/overview")
def get_overview():
    return {"parkingoverview": parking_overview_service.get_overview()}

Report = models.ReportFileModel

@app.post("/report")
def create_report(report: Report):
    report_service.save_report(
        report.id, report.report_name, report.parking_areas, report.date
    )
    return report
