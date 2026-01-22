import architecture as arch


print("Welcome to Adventure Time...")
print("To see the possible commmands type -help")

command = arch.Commands()



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

