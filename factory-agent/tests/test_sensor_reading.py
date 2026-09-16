
from factory_agent.sensor_reading import SensorReading
import datetime

def test_create_SensorReading():
    timestamp = datetime.datetime(1989, 12, 22, 12, 0, 0)
    data = SensorReading(machine_id="machine01", machine_type="robotic arm",
                         temperature_celsius=72, status="running",runtime_seconds=3600,
                         error_code="ERROR: HIGH_TEMP", timestamp=timestamp)

    assert data.machine_id == "machine01"
    assert data.machine_type == "robotic arm"
    assert data.temperature_celsius == 72
    assert data.status == "running"
    assert data.runtime_seconds == 3600
    assert data.error_code == "ERROR: HIGH_TEMP"
    assert data.timestamp == timestamp
    
def test_error_code_can_be_none():
    timestamp = datetime.datetime(1989, 12, 22, 12, 0, 0)
    data = SensorReading(machine_id="machine01", machine_type="robotic arm",
                         temperature_celsius=72, status="running",runtime_seconds=3600,
                         error_code=None, timestamp=timestamp)
    
    assert data.error_code == None
