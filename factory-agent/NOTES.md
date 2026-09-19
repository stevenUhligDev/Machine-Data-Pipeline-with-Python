# Factory Agent - Planning

## Machines

- Robotic arm
- Conveyor belt
- Lift
- Welding robot (planned extension)

## Shared Sensor Data

- `machine_id`
- `machine_type`
- `temperature_celsius`
- `status`
- `runtime_seconds`
- `error_code`
- `timestamp`

These fields are used both by the factory agent and by the backend API.

The agent creates sensor readings internally.

The backend receives sensor readings as JSON data.

## Current Classes

### Machine

Responsibilities:

- stores `machine_id`
- stores `machine_type`
- stores current temperature
- stores current status
- stores `runtime_seconds`
- stores optional `error_code`
- advances runtime and temperature while running
- cools down while sleeping
- checks for overheating
- marks itself as error when overheating occurs

### SensorReading

Responsibilities:

- stores a snapshot of a machine state
- contains all shared sensor data fields
- can be converted into a dictionary with `to_dict()`
- provides JSON-friendly data, including timestamp as ISO string

### Agent

Responsibilities:

- registers machines
- creates sensor readings from machine states
- collects current sensor readings
- keeps a history of collected readings
- runs a simulation cycle with `run_cycle()`

Current cycle order:

1. advance registered machines
2. check for overheating
3. collect sensor readings

### Backend / API

Responsibilities:

- provides a FastAPI application
- exposes a health endpoint with `GET /health`
- exposes a first readings endpoint with `POST /readings`
- receives sensor reading data in JSON format
- validates incoming request bodies with Pydantic
- returns validated reading data for valid requests
- rejects invalid or incomplete requests with validation errors
- stores validated sensor readings temporarily in memory
- provides stored sensor readings through `GET /readings`

## Error Cases

- `machine_id` is missing or empty
- `temperature_celsius` is unrealistically high or low
- `runtime_seconds` is negative
- `status` is not allowed
- unknown `machine_type`
- sensor reading contains missing required fields
- overheated machine is marked with status `error`
- overheated machine receives error code `ERR_OVERHEAT`
- API request body is missing required fields
- API request body contains invalid data types
- backend rejects invalid sensor reading data with status code `422`

## Implemented Tests

- Machine can be initialized
- Machine advances runtime while running
- Machine temperature increases while running
- Machine cools down while sleeping
- Machine detects overheating
- Machine does not overheat below or exactly at the limit
- SensorReading contains all required fields
- SensorReading can be converted to a dictionary
- SensorReading dictionary can be serialized to JSON
- Agent can register machines
- Agent can create sensor readings
- Agent can collect current sensor readings
- Agent keeps a reading history
- Agent run cycle advances machines, checks overheating, and collects readings
- Backend health endpoint returns status code `200`
- Backend health endpoint returns status `ok`
- `POST /readings` accepts valid sensor reading data
- `POST /readings` returns status code `201` for valid data
- `POST /readings` returns the validated reading data
- `POST /readings` rejects missing required fields
- Missing `machine_id` returns status code `422`
- Missing `timestamp` returns status code `422`
- `GET /readings` returns an empty list when no readings exist
- `GET /readings` returns a previously created reading
- API tests use an autouse pytest fixture for isolated in-memory storage

## FastAPI Backend Planning

### Current Backend Structure

The backend is located in the `backend` directory.

The importable Python package is called `factory_backend`.

Current backend structure:

- `backend/src/factory_backend/main.py`
- `backend/src/factory_backend/__init__.py`
- `backend/tests/test_readings_api.py`
- `backend/pyproject.toml`

### Current Backend Goal

The current backend goal is not full data processing yet.

The first goal is to make sure that the API can receive sensor reading data, validate it, and return a predictable response.

Data storage, forwarding, database integration, and authentication are planned for later steps.

### Implemented Endpoints

#### `GET /health`

The health endpoint is used as a simple smoke test.

It checks whether the FastAPI application is reachable.

Expected response:

- status code `200`
- response body contains status `ok`

#### `POST /readings`

The readings endpoint receives sensor reading data in JSON format.

The endpoint currently validates incoming data with a Pydantic model.

Valid sensor readings are accepted.

Invalid or incomplete sensor readings are rejected by FastAPI/Pydantic validation.

#### `GET /readings`

The endpoint returns the sensor readings currently stored in memory.

If no readings exist, it returns an empty list.

### Reading Model

The API uses a Pydantic model called `Reading`.

The model validates the following fields:

- `machine_id`
- `machine_type`
- `temperature_celsius`
- `status`
- `runtime_seconds`
- `error_code`
- `timestamp`

Required fields:

- `machine_id`
- `machine_type`
- `temperature_celsius`
- `status`
- `runtime_seconds`
- `timestamp`

Optional fields:

- `error_code`

### Current API Behavior

A valid sensor reading sent to `POST /readings` should return:

- status code `201`
- the validated reading data in the response body

A sensor reading with a missing required field, for example `machine_id`, should return:

- status code `422`

This validation is handled automatically by FastAPI and Pydantic before the endpoint logic is executed.

The current `POST /readings` endpoint does not store readings permanently yet.

At this stage, it validates the incoming request body and returns the validated reading data.

This keeps the first backend step small and testable.

Accepted readings are currently stored in memory.

The storage is temporary and is cleared when the application restarts.

`GET /readings` can be used to retrieve the currently stored readings.

### Implemented API Tests

- Health endpoint returns status code `200`
- Health endpoint returns status `ok`
- `POST /readings` accepts a valid sensor reading
- `POST /readings` returns status code `201` for valid data
- `POST /readings` returns the validated reading data
- `POST /readings` rejects a request with missing `machine_id`
- Invalid request data returns status code `422`
- `POST /readings` rejects a request with missing `timestamp`
- `GET /readings` returns an empty list when no readings exist
- `GET /readings` returns a previously created reading
- API tests use isolated in-memory storage

## Problem Documentation

### Separate In-Memory Lists

Problem:
The storage test remained empty after sending a reading.

Cause:
The endpoint and the test initially used separate local lists.

Solution:
The shared `sensor_readings` list was moved to module level.

Learning:
Shared application state must be accessible by all components that use it.

### UnboundLocalError with `sensor_readings`

Problem:
Accessing `sensor_readings` caused an `UnboundLocalError`.

Cause:
The module-level list was deleted inside the endpoint with `del`.

Solution:
The existing list is now modified directly with `append()`.

Learning:
A mutable module-level object can be modified without recreating or deleting it.

### Shared Test State

Problem:
API tests could influence each other because they used the same in-memory storage.

Solution:
An autouse pytest fixture clears the storage before and after every API test.

Learning:
Tests should start with a defined state and should not depend on execution order.

## Current Learning Focus

- difference between Python dictionaries and JSON
- converting internal Python objects into JSON-friendly data
- understanding HTTP `POST` requests
- understanding FastAPI endpoints
- using Pydantic models for request body validation
- testing API behavior with `TestClient`
- distinguishing valid requests from invalid requests
- understanding in-memory storage
- understanding test isolation with pytest fixtures
- understanding basic Create and Read API behavior

## Next Steps

- Connect the Factory Agent to the FastAPI backend using HTTP.
- Send generated sensor readings from the agent to `POST /readings`.
- Test the first complete data flow from machine simulation to backend.
- Refactor backend responsibilities after the basic end-to-end data flow is working.