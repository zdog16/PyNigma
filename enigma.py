from rich.traceback import install
from rich.console import Console
import yaml
c = Console()

install()

with open("properties.yml", "r") as file:
    properties = yaml.safe_load(file)

class rotor:
    def __init__(self, wheelPosition, rotor, startIndex) -> None:
        self.wheelPosition = wheelPosition
        self.rotation = startIndex
        self.inSide = properties["Rotor " + rotor + " Input"]
        self.outSide = properties["Rotor " + rotor + " Output"]
        self.notch = properties["Rotor " + rotor + " Notch"]
        
    def rotate(self):
        if self.wheelPosition == 1:
            if self.rotation == 26:
                self.rotation = 1
            else:
                self.rotation += 1
        else:
            pass
    
    def passthrough(self, charIn):
        letterOut = self.outSide[self.inSide.index(charIn)]
        self.rotate()
        return letterOut

    def loopThrough(self, charIn):
        return self.inSide[self.outSide.index(charIn)]

class reflector:
    def __init__(self) -> None:
        self.inSide = properties["Reflector In"]
        self.outSite = properties["Reflector Out"]