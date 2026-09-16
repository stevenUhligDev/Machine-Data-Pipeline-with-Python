# Machine Data Pipeline with Python


## Project Goal

- short explain: safe IoT-Data-Pipeline for a simulated Factory environment


## Learning Goals

- Python

- REST APIs

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

- Phase 1: Factory Agent is in progress.
  
- Local Python project setup is complete.
  
- Basic package structure with `src` layout is working.
  
- `Machine`, `SensorReading`, and `Agent` are implemented.
  
- Unit tests with pytest are passing.
  
- The agent can register machines, create sensor readings, collect current readings, and keep a reading history.
  
- Sensor reading creation was refactored from `Machine` into `Agent` to improve separation of responsibilities.

- `run_cycle` is implemented and tested

- A cycle currently advances registered machines, checks for overheating and then collects sensor readings.

- Overheated machines are marked with status `error` and error_code `ERR_OVERHEAT` before sensor readings are created

- Tests cover machine behavior, sensor reading creation, reading collections, history handling, and the agent run cycle
