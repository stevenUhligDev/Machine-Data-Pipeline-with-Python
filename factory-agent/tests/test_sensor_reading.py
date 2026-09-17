from factory_agent.sensor_reading import SensorReading
from factory_agent.agent import Agent
from factory_agent.machine import Machine
import pytest
import datetime
import json

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
    
def test_sensor_reading_can_be_converted_to_dict():
    
    
    agent = Agent()
    machine = Machine("Maschine01", "Lift", 65.3, "running", 3600)
    
    data = agent.create_sensor_reading(
        machine
    )
    
    reading_dict = data.to_dict()
    
    assert reading_dict["machine_id"] == "Maschine01"
    assert reading_dict["machine_type"] == "Lift"
    assert reading_dict["temperature_celsius"] == 65.3
    assert reading_dict["status"] == "running"
    assert reading_dict["runtime_seconds"] == 3600
    assert reading_dict["error_code"] is None
    assert reading_dict["timestamp"] == "2026-09-15T00:00:00"
    
def test_sensor_reading_dict_can_be_serialized_to_json():
    
    agent = Agent()
    machine = Machine("Maschine01", "Lift", 65.3, "running", 3600)
    
    data = agent.create_sensor_reading(
        machine
    )
    
    reading_dict = data.to_dict()
    json_txt = json.dumps(reading_dict)
    json_to_dict = json.loads(json_txt)
    
    assert isinstance(json_txt, str)
    assert isinstance(json_to_dict, dict)
    
    assert json_to_dict["machine_id"] == "Maschine01"
    assert json_to_dict["machine_type"] == "Lift"
    assert json_to_dict["temperature_celsius"] == pytest.approx(65.3)
    assert json_to_dict["status"] == "running"
    assert json_to_dict["runtime_seconds"] == 3600
    assert json_to_dict["error_code"] is None
    assert json_to_dict["timestamp"] == "2026-09-15T00:00:00"
    
    
    