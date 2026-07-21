from factory_agent.agent import FactoryAgent
from factory_agent.machine import Machine

def test_init_agent():
    agent = FactoryAgent()
    
    assert len(agent.machines) == 0
    
    

def test_add_machine():
    machine1 = Machine("Maschine01", "Lift", 65.3, "running", 3600)
    machine2 = Machine("Maschine02", "robotic arm", 60.0, "running", 2100)
    agent = FactoryAgent()
    
    agent.add_machine(machine1)
    agent.add_machine(machine2)
    
    assert agent.machines[0] == machine1
    assert agent.machines[1] == machine2
    assert len(agent.machines) == 2