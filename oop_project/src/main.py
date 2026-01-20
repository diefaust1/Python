import architecture as arch, time


print("Welcome to Adventure Time...")
print("To see the possible commmands type -help")

command = arch.Commands()
MINIMAL_GOLD = 5
gold = 0

start_time = time.monotonic()

while True:
    
    current_time = time.monotonic()
    time_passed = current_time - start_time
    gold = gold + time_passed
    start_time = current_time

    user_input = input()
    match user_input:
        
        case command.HELP:
            command.help_command()
        
        case command.EXIT:
            break
        
        case command.CLEAR:
            command.clear_terminal()
        
        case "-gold":
            print(round(gold, 3))
        
        case _:
            print("command not found")

