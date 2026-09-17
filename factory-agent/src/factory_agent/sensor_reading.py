import datetime
from dataclasses import dataclass





@dataclass
class SensorReading:
	machine_id: str
	machine_type: str
	temperature_celsius: float
	status: str
	runtime_seconds: int
	error_code: str | None
	timestamp: datetime.datetime
 
	def to_dict(self):
		return {
			"machine_id": self.machine_id,
			"machine_type": self.machine_type,
			"temperature_celsius": self.temperature_celsius,
			"status": self.status,
			"runtime_seconds": self.runtime_seconds,
			"error_code": self.error_code,
			"timestamp": self.timestamp.isoformat(),
		}
 
 


