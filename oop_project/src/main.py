import subprocess, os, sys
import character_classes as char_class

class Commands:

    HELP = "-help"
    EXIT = "-exit"
    CLEAR = "-clear"
    INVENTORY = "-inv"
    CHARACTER = "-char"
    QUEST = "-quest"
    
    DESCRIPTION = {
        HELP:"shows all available commands",
        EXIT: "exits the game",
        CLEAR: "clears the terminal from prior output",
        INVENTORY: "shows the players inventory",
        CHARACTER: "shows the characters stats",
        QUEST: "shows one of three quest that you can embark on"
    }
    
    def character_stats(self, character: char_class.BaseCharacter):
        temp_dict = character.stats()
        for key, value in temp_dict.items():
            print(f"{key}: {value}")

    @classmethod
    def help_command(cls):
        for key, value in cls.DESCRIPTION.items():
            print(f"{key}: {value}")
    
    def clear_terminal(self):
        command = "cls" if os.name == "nt" else "clear"
        subprocess.run(command, shell=True)

    # Start of Game
def main():
    #variables and objects
    command = Commands()
    character = None
    choose_class = 0
    number_of_classes = 3

    print("Welcome to Adventure Time...")

    choose_name = input("How do you like to be called?\n")

    while choose_class < 1 or choose_class > number_of_classes:
        try:
            choose_class = int(input("Choose a class, write the number\n1) Peasant\n\n2) Knight\n\n3) Warrior\n"))
        except ValueError:
            print("Please enter a valid number")
            
    match choose_class:
        case 1: 
            character = char_class.Peasant(choose_name)
        case 2: 
            character = char_class.Knight(choose_name)
        case 3: 
            character = char_class.Warrior(choose_name)
        case _: 
                print("ClassError")

    # Main Game Loop
    print("Character created...\nTo see the possible commmands type -help")
    while True:
        
        user_input = input()
        match user_input:
            
            case command.HELP:
                command.help_command()
            
            case command.EXIT:
                break
            
            case command.CLEAR:
                command.clear_terminal()
            
            case command.CHARACTER:
                if character is None:
                    print("Character not created, abort game...")
                    sys.exit()
                else:
                    command.character_stats(character)
            
            case "-gold":
                print()
            
            case _:
                print("command not found")

if __name__ == "__main__":
    main()



