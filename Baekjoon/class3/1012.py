import sys
input = sys.stdin.readline

T = int(input().rstrip())
move = [(0,1), (0,-1), (1,0), (-1,0)]
maps = set()
visited = set()

def dfs(x, y):
    stack = [(x, y)]
    visited.add((x, y))
    while stack:
        x, y = stack.pop()
        for dx, dy in move:
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_x >= COL or new_y < 0 or new_y >= ROW:
                continue
            if (new_x, new_y) not in maps:
                continue
            if (new_x, new_y) in visited:
                continue
            visited.add((new_x, new_y))
            stack.append((new_x, new_y))
    return 1


for _ in range(T):
    COL, ROW, CABBAGE = map(int, input().split(" "))
    maps.clear()
    visited.clear()
    answer = 0

    for _ in range(CABBAGE):
        maps.add(tuple(map(int, input().split(" "))))

    for x, y in maps:
        if (x, y) not in visited:
            answer += dfs(x, y)
    
    print(answer)