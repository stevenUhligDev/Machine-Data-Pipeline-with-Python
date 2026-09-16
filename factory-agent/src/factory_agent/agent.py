import datetime

from factory_agent import sensor_reading
from factory_agent.machine import Machine


class Agent:
    
    def __init__(self):
        self.machines = []
        self.sensor_readings = []
    
    def add_machine(self,machine):
        self.machines.append(machine)
        
    def create_sensor_reading(self, machine: Machine):
        timestamp = datetime.datetime(2026, 9, 15, 0, 0)
        data = sensor_reading.SensorReading(
            machine.machine_id,
            machine.machine_type,
            machine.temperature_celsius,
            machine.status,
            machine.runtime_seconds,
            machine.error_code,
            timestamp=timestamp,
        )
        return data
        
    def collect_sensor_readings(self):
        current_sensor_readings = []
        for machine in self.machines:
            data = self.create_sensor_reading(machine)
            self.sensor_readings.append(data)
            current_sensor_readings.append(data)
        
        return current_sensor_readings
    
    def run_cycle(self):
        for machine in self.machines:
            machine.advance_time()
            machine.check_overheat()
        current_sensor_readings = self.collect_sensor_readings()
        return current_sensor_readings
              
        
            
            
        
            
            
    
    