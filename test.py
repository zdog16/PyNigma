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

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alph_list = []
for i in alphabet:
    alph_list.append(i)

scramble = ""
for i in range(1, 27):
    char = random.choice(alph_list)
    scramble = scramble + char
    alph_list.remove(char)

c.print(scramble)
pyperclip.copy(scramble)