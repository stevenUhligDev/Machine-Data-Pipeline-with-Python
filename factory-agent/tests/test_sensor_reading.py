
from factory_agent.sensor_reading import SensorReading

def test_create_SensorReading():
    data = SensorReading(machine_id="machine01", machine_type="robotic arm", temperature_celsius=72, status="enable",runtime_seconds=3600, error_code="", timestamp="1989-12-22 12:00:00")

    assert data.machine_id == "machine01"
    assert data.machine_type == "robotic arm"
    assert data.temperature_celsius == 72
    assert data.status == "enable"
    assert data.runtime_seconds == 3600
    assert data.error_code == ""
    assert data.timestamp == "1989-12-22 12:00:00"