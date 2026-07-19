# Factory Agent

## Purpose

- The agent simulates machinedata for a factory environment

## Simulatet Machines

- Robotic arm

- Conveyor belt

- Lift

- Welding robot planned as future extension

## Sensor Data

- machine_id

- machine_type

- temperature_celsius

- status

- runtime_seconds

- error_code

- timestamp

## Plannes Python Components

- Machine

- SensorReading

- FactoryAgent


## First Test Ideas

- Machine can generate a SensorReading

- SensorReading contains all required fields

- temperature_celsius is within a realistic range

- runtime_seconds is never negative

- unknown machine_type is handled safe
