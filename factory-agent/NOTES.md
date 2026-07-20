# Factory Agent - Planning

## Maschines
- Robotic arm
- Conveyor belt
- Lift
- Welding robot (planned extention)


## Shared Sensor Data
- machine_id
- machine_type
- temperature_celsius
- status
- runtime_seconds
- error_code
- timestamp


## Possible Classees
# Machine
- Machine responsibilities:
    - stores machine_id
    - stores machine_type
    - stores current temperature
    - stores current status
    - stores runtime_seconds
    - can create a SensorReading from its current state
    - SensorReading
    - FactoryAgent


## Error cases
- machine_id is missing or empty
- temperature_celsius unrealistically high or low
- runtime_seconds is never negative
- status not allowed
- unknown machine_type
- sensor reading contains missing required fields
- 


## First tests
- machine can generate a SensorReading
- SensorReading contains all required fields
- temperature_celsius is within a realistic range
- runtime_seconds is never negativ
- unknow machine_type is handled safely
- missing machine_id rejected
