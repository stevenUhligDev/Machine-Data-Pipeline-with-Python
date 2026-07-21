from factory_agent.machine import Machine
import datetime
import pytest

def test_init_machine():
    
    machine = Machine("Maschine01", "Lift", 65.3, "running", 3600)
    
    assert machine.machine_id == "Maschine01"
    assert machine.machine_type == "Lift"
    assert machine.temperature_celsius == 65.3
    assert machine.status == "running"
    assert machine.runtime_seconds == 3600
    
def test_create_sensor_reading():
    timestamp = datetime.datetime(1989, 12, 22, 12, 0, 0)
    
    machine = Machine("Maschine01", "Lift", 65.3, "running", 3600)
    data = machine.create_sensor_reading()
    
    assert data.machine_id == "Maschine01"
    assert data.machine_type == "Lift"
    assert data.temperature_celsius == 65.3
    assert data.status == "running"
    assert data.runtime_seconds == 3600
    assert data.error_code is None
    assert data.timestamp == timestamp
    
def test_advance_time():
    machine = Machine("Maschine01", "Lift", 65.3, "sleep", 3600)
    machine.set_state_running()
    machine.advance_time()
    
    assert machine.runtime_seconds == 3660
    assert machine.temperature_celsius == 65.8
    
def test_sleep_and_cool_down():
    machine = Machine("Maschine01", "Lift", 70.3, "running", 3750)
    machine.set_state_sleep()
    machine.advance_time()
    
    assert machine.runtime_seconds == 3750
    assert machine.temperature_celsius == pytest.approx(70.0)
    
def test_error_overheat():
    machine = Machine("Maschine01", "Lift", 80.3, "running", 3750)
    machine.check_overheat()
    data = machine.create_sensor_reading()
    
    assert machine.status == "error"
    assert machine.error_code == "ERR_OVERHEAT"
    assert data.status == "error"
    assert data.error_code == "ERR_OVERHEAT"
    
          
    
    
