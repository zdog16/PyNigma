from rich.traceback import install
from rich.console import Console
from rich.prompt import Prompt
import enigma
install()
c = Console()

def split(str_in):
    out_list = []
    for i in str_in:
        out_list.append(i.upper())
    return out_list


wheel1 = enigma.rotor(1, "I", 10)
wheel2 = enigma.rotor(2, "II", 11)
wheel3 = enigma.rotor(3, "III", 14)
reflector = enigma.reflector()

def encryptChar(char):
    wheel2.rotate()
    step1 = wheel2.passthrough(char)
    c.print(step1)
    step2 = wheel1.passthrough(step1)
    c.print(step2)
    step3 = reflector.passthrough(step2)
    c.print(step3)
    step4 = wheel1.passthrough(step3, loop=True)
    c.print(step4)
    step5 = wheel2.passthrough(step4, loop=True)
    c.print(step5)
    return step5



def encrypt(msg):
    msg_list = split(msg)

    outMsg = ""
    for i in msg_list:
        outMsg = outMsg + encryptChar(i)
    
    return outMsg


message = Prompt.ask("Enter Message")
c.print(encrypt(message))

