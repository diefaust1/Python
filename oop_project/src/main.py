import subprocess, os, character_classes

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


print("Welcome to Adventure Time...")
print("To see the possible commmands type -help after the character creation")

command = Commands()

choose_name = input("How do you like to be called?")

choose_class = input("Choose a class, write the number - 1) Peasant ")

match choose_class:
    case 1: 
        character = character_classes.Peasant
    case _:
            print("Class not found")


while True:
    
  

    user_input = input()
    match user_input:
        
        case command.HELP:
            command.help_command()
        
        case command.EXIT:
            break
        
        case command.CLEAR:
            command.clear_terminal()
        
        case "-gold":
            print()
        
        case _:
            print("command not found")



