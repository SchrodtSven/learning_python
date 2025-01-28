#   0 1 0 1 1 1 0
#   0 1 1 1 1 1 0 
#   0 1 1 1 1 1 1
#   1 0 0
#   
#
#
command = ''
stop_actions = ['quit', 'stop', 'exit']

while command not in (stop_actions):
    command = input("What are you doing next? ")
    match command.split():
        case [action]:
            print(f"action without object: {action=}")
        case [action, obj]:
            print(f"{action=}, {obj=}")
            
# https://python-kurs.eu/abenteuer-spiel-mit-strukturellem-pattern-matching.php
# https://www.freecodecamp.org/news/how-i-developed-my-first-game/

        