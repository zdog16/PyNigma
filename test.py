from rich.traceback import install
from rich.console import Console
import yaml
c = Console()

def buildProperties():
    wheel1Input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    wheel1Output = "QWERTYUIOPASDFGHJKLZXCVBNM"
    setProperties = {"Wheel1Input": wheel1Input, "Wheel1Output": wheel1Output}

    with open("properties.yml", "w") as file:
        yaml.dump(setProperties, file)

with open("properties.yml", "r") as file:
    properties = yaml.safe_load(file)
c.print(properties)