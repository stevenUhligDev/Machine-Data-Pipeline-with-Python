from factory_agent.agent import Agent
from factory_agent.machine import Machine
from factory_agent import sensor_reading
import datetime


def test_init_agent():
    agent = Agent()
    
    assert len(agent.sensor_readings) == 0
    assert len(agent.machines) == 0
    

def test_add_machine():
    machine1 = Machine("Maschine01", "Lift", 65.3, "running", 3600)
    machine2 = Machine("Maschine02", "robotic arm", 60.0, "running", 2100)
    agent = Agent()
    
    agent.add_machine(machine1)
    agent.add_machine(machine2)
    
    assert agent.machines[0] == machine1
    assert agent.machines[1] == machine2
    assert len(agent.machines) == 2


def test_create_sensor_reading():
    agent = Agent()
    machine = Machine("Maschine01", "Lift", 65.3, "running", 3600)
    
    data = agent.create_sensor_reading(
        machine
    )
    
    assert isinstance(data, sensor_reading.SensorReading)
    assert data.machine_id == "Maschine01"
    assert data.machine_type == "Lift"
    assert data.temperature_celsius == 65.3
    assert data.status == "running"
    assert data.runtime_seconds == 3600
    assert data.error_code is None
    assert data.timestamp == datetime.datetime(2026, 9, 15, 0, 0)
    
        
def test_collect_sensor_readings():
    machine1 = Machine("Maschine01", "Lift", 65.3, "running", 3600)
    machine2 = Machine("Maschine02", "robotic arm", 60.0, "running", 2100)
    agent = Agent()
    agent.add_machine(machine1)
    agent.add_machine(machine2)
    current_readings = agent.collect_sensor_readings()
    
    assert len(current_readings) == 2
    assert len(agent.machines) == 2
    assert len(agent.sensor_readings) == 2
    assert current_readings[0].machine_id == "Maschine01"
    assert current_readings[1].machine_type == "robotic arm"
    assert agent.sensor_readings[0].machine_id == "Maschine01"
    assert agent.sensor_readings[1].machine_type == "robotic arm"
    assert agent.machines[0].machine_id == "Maschine01"
    assert agent.machines[1].machine_type == "robotic arm"
    
    assert isinstance(current_readings[0], sensor_reading.SensorReading)
    assert isinstance(current_readings[1], sensor_reading.SensorReading)