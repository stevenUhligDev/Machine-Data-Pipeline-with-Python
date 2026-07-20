from factory_agent.machine import Machine
import datetime

def test_create_machine():
    
    machine = Machine("Maschine01", "Lift", 65.3, "running", 3600)
    
    assert machine.machine_id == "Maschine01"
    assert machine.machine_type == "Lift"
    assert machine.temperature_celsius == 65.3
    assert machine.status == "running"
    assert machine.runtime_seconds == 3600
    
def test_machine_create_sensor_reading():
    timestamp = datetime.datetime(1989, 12, 22, 12, 0, 0)
    
    machine = Machine("Maschine01", "Lift", 65.3, "running", 3600)
    data = machine.create_sensor_reading()
    
    assert data.machine_id == "Maschine01"
    assert data.machine_type == "Lift"
    assert data.temperature_celsius == 65.3
    assert data.status == "running"
    assert data.runtime_seconds == 3600
    assert data.error_code == None
    assert data.timestamp == timestamp
    
    