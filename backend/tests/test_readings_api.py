from fastapi.testclient import TestClient
from factory_backend.main import app, Reading



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
    assert response.json()["error_code"] == None
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
    print(response.json())
    assert response.status_code == 422

    