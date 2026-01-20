import subprocess
import os

class Commands:

    HELP = "-help"
    EXIT = "-exit"
    CLEAR = "-clear"
    GOLD = "-gold"
    
    DESCRIPTION = {
        HELP:"shows all available commands",
        EXIT: "exits the game",
        CLEAR: "clears the terminal from prior output",
        GOLD: "shows the players gold"
    }

    @classmethod
    def help_command(cls):
        for key, value in cls.DESCRIPTION.items():
            print(f"{key}: {value}")
    
    def clear_terminal(self):
        command = "cls" if os.name == "nt" else "clear"
        subprocess.run(command, shell=True)

    def show_gold(gold):
        print(str(gold) + " gold")
