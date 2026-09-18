from fastapi import FastAPI, HTTPException
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

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/readings", status_code=201)
async def readings(reading: Reading):
    return reading