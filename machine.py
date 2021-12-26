from rich.traceback import install
from rich.console import CONSOLE_HTML_FORMAT, Console
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









to_encrypt = Prompt.ask("Enter Message to translate")
to_encrypt_list = split(to_encrypt)
