from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import report_service, parkingarea_service, models

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


@app.get("/report")
def get_report():
    return {"report": report_service.create_report()}

@app.get("/parkingareas")
def get_parking_areas():
    return {"parkingareas": parkingarea_service.all_parking_areas()}

Report = models.ReportModel

@app.post("/report")
def create_report(report: Report):
    return report