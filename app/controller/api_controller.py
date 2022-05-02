from fastapi import FastAPI

app = FastAPI(title="FastAPI, Docker, and Traefik")


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/report")
def get_report():
    return {"report": "belægningsgrad"}