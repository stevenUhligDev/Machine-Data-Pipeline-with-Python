import datetime
from factory_agent import sensor_reading

class Machine:
    def __init__(self, machine_id: str, machine_type: str,
                 temperature_celsius: float, status: str,
                 runtime_seconds: int):
        
        self.machine_id = machine_id
        self.machine_type = machine_type
        self.temperature_celsius = temperature_celsius
        self.status = status
        self.runtime_seconds = runtime_seconds
        
    def create_sensor_reading(self):
        timestamp = datetime.datetime(1989, 12, 22, 12, 0, 0)
        data = sensor_reading.SensorReading(self.machine_id, self.machine_type,
                                            self.temperature_celsius, self.status,
                                            self.runtime_seconds, error_code=None,
                                            timestamp=timestamp)
        return data        
                
