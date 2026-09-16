import random

machine_states = ["RUNNING", "IDLE", "ERROR"]

def generate_machine_state():
    return random.choices(machine_states, weights=[70, 20, 10])[0]
     

def generate_temerature(a, b):
    return round(random.uniform(a, b), 1)

current_state = generate_machine_state()
current_temperature = generate_temerature(20.0, 100.0)
print(f"Aktueller Maschinenstatus: {current_state}")
print(f"Aktuelle Temperatur: {current_temperature} °C")
