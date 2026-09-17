# Factory Agent - Planning

## Machines

- Robotic arm
- Conveyor belt
- Lift
- Welding robot (planned extension)

## Shared Sensor Data

- machine_id
- machine_type
- temperature_celsius
- status
- runtime_seconds
- error_code
- timestamp

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

## Error Cases

- `machine_id` is missing or empty
- `temperature_celsius` is unrealistically high or low
- `runtime_seconds` is negative
- `status` is not allowed
- unknown `machine_type`
- sensor reading contains missing required fields
- overheated machine is marked with status `error`
- overheated machine receives error code `ERR_OVERHEAT`

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