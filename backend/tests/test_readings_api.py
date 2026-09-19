import pytest
from fastapi.testclient import TestClient
from factory_backend.main import app, sensor_readings

@pytest.fixture(autouse=True)
def clear_sensor_readings():
    sensor_readings.clear()
    yield
    sensor_readings.clear()



def test_health_endpoint_returns_ok():
    client = TestClient(app)
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    
def test_post_reading_accepts_valid_sensor_reading():
    client = TestClient(app)
    data = {
        "machine_id": "Maschine01",
        "machine_type": "Lift",
        "temperature_celsius": 76,
        "status": "running",
        "runtime_seconds": 600,
        "error_code": None,
        "timestamp": "2026-09-17T06:00:00"
    }
    
    response = client.post("/readings", json=data)
    
    assert response.status_code == 201
    assert response.json()["machine_id"] == "Maschine01"
    assert response.json()["machine_type"] == "Lift"
    assert response.json()["temperature_celsius"] == 76
    assert response.json()["status"] == "running"
    assert response.json()["runtime_seconds"] == 600
    assert response.json()["error_code"] is None
    assert response.json()["timestamp"] == "2026-09-17T06:00:00"

    
def test_post_reading_rejects_missing_machine():
    client = TestClient(app)
    data = {
            "machine_type": "Lift",
            "temperature_celsius": 76,
            "status": "running",
            "runtime_seconds": 600,
            "error_code": None,
            "timestamp": "2026-09-17T06:00:00"
        }
    
    response = client.post("/readings", json=data)
    assert response.status_code == 422
    
def test_post_reading_rejects_missing_timestamp():
    client = TestClient(app)
    data = {
            "machine_id": "Maschine01",
            "machine_type": "Lift",
            "temperature_celsius": 76,
            "status": "running",
            "runtime_seconds": 600,
            "error_code": None,
        }
    
    response = client.post("/readings", json=data)
    assert response.status_code == 422

def test_post_readings_save_reading_in_memory_storage_sensor_readings():
    client = TestClient(app)
    data = {
            "machine_id": "Maschine01",
            "machine_type": "Lift",
            "temperature_celsius": 76,
            "status": "running",
            "runtime_seconds": 600,
            "error_code": None,
            "timestamp": "2026-09-17T06:00:00"
        }
    client.post("/readings", json=data)
    assert len(sensor_readings) == 1
    
def test_get_readings_returns_empty_list_when_no_readings_exist():
    client = TestClient(app)
    
    response = client.get("/readings")
    
    assert response.status_code == 200
    assert response.json() == []
    
def test_get_readings_returns_previously_created_reading():
    client = TestClient(app)
    data = {
            "machine_id": "Maschine01",
            "machine_type": "Lift",
            "temperature_celsius": 76,
            "status": "running",
            "runtime_seconds": 600,
            "error_code": None,
            "timestamp": "2026-09-17T06:00:00"
        }
    client.post("/readings", json=data)
    response = client.get("/readings")
    
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["machine_id"] == "Maschine01"
    assert response.json()[0]["machine_type"] == "Lift"
    assert response.json()[0]["temperature_celsius"] == 76
    assert response.json()[0]["status"] == "running"
    assert response.json()[0]["runtime_seconds"] == 600
    assert response.json()[0]["error_code"] is None
    assert response.json()[0]["timestamp"] == "2026-09-17T06:00:00"
    
    