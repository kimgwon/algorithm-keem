import sys
input = sys.stdin.readline

M = int(input().strip())
s = set()

while M > 0:
    M -= 1
    commands = input().strip().split(" ")

    if commands[0] == "all":
        s = {i for i in range(1, 21)}
    elif commands[0] == "empty":
        s.clear()

    if len(commands) <= 1:
        continue
    
    command, x = commands[0], int(commands[1])

    if command == "add":
        s.add(x)
    elif command == "check":
        print(1 if x in s else 0)
    elif command == "remove":
        s.discard(x)
    elif command == "toggle":
        s.remove(x) if x in s else s.add(x)