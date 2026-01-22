import subprocess
import os

class Commands:

    HELP = "-help"
    EXIT = "-exit"
    CLEAR = "-clear"
    INVENTORY = "-inv"
    CHARACTER = "-char"
    
    DESCRIPTION = {
        HELP:"shows all available commands",
        EXIT: "exits the game",
        CLEAR: "clears the terminal from prior output",
        INVENTORY: "shows the players inventory"
    }

    @classmethod
    def help_command(cls):
        for key, value in cls.DESCRIPTION.items():
            print(f"{key}: {value}")
    
    def clear_terminal(self):
        command = "cls" if os.name == "nt" else "clear"
        subprocess.run(command, shell=True)

