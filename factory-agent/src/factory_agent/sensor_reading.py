from dataclasses import dataclass 
from datetime import datetime


@dataclass
class SensorReading:
	machine_id: str
	machine_type: str
	temperature_celsius: float
	status: str
	runtime_seconds: int
	error_code: str | None
	timestamp: datetime
 

