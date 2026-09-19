from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


class Reading(BaseModel):
    machine_id: str
    machine_type: str
    temperature_celsius: float
    status: str
    runtime_seconds: int
    error_code: str | None = None
    timestamp: datetime
        
app = FastAPI()

sensor_readings = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/readings", status_code=200)
async def get_readings():
    return sensor_readings

@app.post("/readings", status_code=201)
async def post_readings(reading: Reading):
    sensor_readings.append(reading)
    return reading