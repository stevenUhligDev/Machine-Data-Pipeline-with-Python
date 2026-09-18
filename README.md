# Machine Data Pipeline with Python


## Project Goal

- short explain: safe IoT-Data-Pipeline for a simulated Factory environment


## Learning Goals

- Python

- REST APIs

- FastAPI

- Pydantic validation

- Docker

- CI/CD

- Security scanning

- Logging

- AWS basics

- Infrastructure as code


## Project Phases

1. Factory Agent

2. FastAPI Backend

3. Docker and Docker Compose

4. CI/CD

5. AWS Minimal Deployment

6. Compliance Scanner

7. Infrastructure as Code


## Current Status

### Phase 1: Factory Agent is mostly complete.

- Local Python project setup is complete.

- Basic package structure with `src` layout is working.

- `Machine`, `SensorReading`, and `Agent` are implemented.

- Unit tests with pytest are passing.

- The agent can register machines, create sensor readings, collect current readings, and keep a reading history.

- Sensor reading creation was refactored from `Machine` into `Agent` to improve separation of responsibilities.

- `run_cycle()` is implemented and tested.

- A cycle currently advances registered machines, checks for overheating, and then collects sensor readings.

- Overheated machines are marked with status `error` and error code `ERR_OVERHEAT` before sensor readings are created.

- `SensorReading` can be converted into a dictionary with `to_dict()`.

- Sensor readings can be serialized from dictionary format into JSON and loaded back into a Python dictionary.

### Phase 2: FastAPI Backend has been started.

- A separate `backend` package with `src` layout has been created.

- FastAPI, Pydantic, Uvicorn, and HTTPX have been added as backend-related dependencies.

- A basic health endpoint `GET /health` is implemented and tested.

- The endpoint `POST /readings` is implemented as a first version.

- Incoming sensor reading data is validated with a Pydantic model.

- Valid sensor readings are accepted with status code `201`.

- Invalid sensor readings with missing required fields are rejected with status code `422`.

- Tests cover machine behavior, sensor reading creation, reading collection, history handling, run cycle behavior, dictionary conversion, JSON
  serialization, API health checks, successful reading submission, and validation errors.