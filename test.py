from rich.traceback import install
from rich.console import Console
import pyperclip
import random
import yaml
c = Console()

def buildProperties():
    wheel1Input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    wheel1Output = "QWERTYUIOPASDFGHJKLZXCVBNM"
    setProperties = {"Wheel1Input": wheel1Input, "Wheel1Output": wheel1Output}

    with open("properties.yml", "w") as file:
        yaml.dump(setProperties, file)

def oldStuff():
    with open("properties.yml", "r") as file:
        properties = yaml.safe_load(file)
    c.print(properties)

list_in = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
list_out = []
for i in range(0, 25):
    choice = random.choice(list_in)
    list_out.append(choice)
    list_in.remove(choice)

c.print(list_out)