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
        self.error_code = None
        
    def create_sensor_reading(self):
        timestamp = datetime.datetime(1989, 12, 22, 12, 0, 0)
        data = sensor_reading.SensorReading(self.machine_id, self.machine_type,
                                            self.temperature_celsius, self.status,
                                            self.runtime_seconds, self.error_code,
                                            timestamp=timestamp)
        return data      
    
    def advance_time(self):
        match self.status:
            case "running":
                self.increment_runtime()
                self.heat_up_temperature()
            
            case "sleep":
                self.cool_down_temperature()
    
    def increment_runtime(self):
        self.runtime_seconds += 60
    
    def heat_up_temperature(self):
        self.temperature_celsius += 0.5
        
    def cool_down_temperature(self):
        self.temperature_celsius -= 0.3
        
    def set_state_running(self):
        self.status = "running"
        
    def set_state_sleep(self):
        self.status = "sleep"         
    
    def check_overheat(self):
        if self.temperature_celsius > 80:
            self.mark_overheat()
    
    def mark_overheat(self):
        self.status = "error"
        self.error_code = "ERR_OVERHEAT"
               
                
       
                
