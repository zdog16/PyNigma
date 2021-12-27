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
        if self.wheelPosition == 2:
            if self.rotation == 26:
                self.rotation = 1
            else:
                self.rotation += 1
        else:
            pass
    
    def passthrough(self, charIn, loop=False):
        if not loop:
            inIndex = self.inSide.index(charIn)
        else:
            inIndex = self.outSide.index(charIn)

        outIndex = inIndex + self.rotation
        try:
            letterOut = self.outSide[outIndex]
        except IndexError:
            outIndex = outIndex - 26
            
        if not loop:
            letterOut = self.outSide[outIndex]
        else:
            letterOut = self.inSide[outIndex]

        return letterOut

    def loopThrough(self, charIn):
        return self.inSide[self.outSide.index(charIn)]

class reflector:
    def __init__(self) -> None:
        self.inSide = properties["Reflector In"]
        self.outSite = properties["Reflector Out"]

    def passthrough(self, charIn):
        return self.inSide[self.inSide.index(charIn)]