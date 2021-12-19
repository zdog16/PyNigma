from rich.traceback import install
from rich.console import Console
import yaml
c = Console()

install()

with open("properties.yml", "r") as file:
    properties = yaml.safe_load(file)

class rotor:
    def __init__(self, number, startIndex) -> None:
        self.rotation = startIndex
        if number == 1:
            self.inSide = properties.wheel1Input
            self.outSide = properties.wheel1Output
            self.advanceIndex = properties.wheel1Index
        elif number == 2:
            self.inSide = properties.wheel2Input
            self.outSide = properties.wheel2Output
            self.advanceIndex = properties.wheel2Index
        
    def passthrough(self, charIn):
        return  self.outSide[self.inSide.index(charIn)]
    def loopThrough(self, charIn):
        return self.inSide[self.outSide.index(charIn)]
    


