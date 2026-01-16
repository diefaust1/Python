import architecture as arch

print("Welcome to Adventure Time...")
print("To see the possible commmands type -help")

command = arch.Commands()

def help_command():
    for key, value in command.DESCRIPTION.items():
        print(key, value)

while(True):
    
    user_input = input()
    match user_input:
        case command.HELP:
            help_command()
        
        case "-exit":
            break
        case _:
            print("command not found")

