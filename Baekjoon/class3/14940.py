import sys
from collections import deque
input = sys.stdin.readline

ROW, COLUMN = map(int, input().split(" "))
maps = []
move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
goal = [0, 0]
answer = [[0 for _ in range(COLUMN)] for _ in range(ROW)]

for i in range(ROW):
    col = list(map(int, input().split(" ")))
    for j in range(len(col)):
        if col[j] == 2:
            goal[0] = j
            goal[1] = i
    maps.append(col)

queue = deque()
queue.append((goal[0], goal[1]))

while queue:
    x, y = queue.popleft()
    for dx, dy in move:
        new_x = x + dx
        new_y = y + dy
        if new_x < 0 or new_x >= COLUMN or new_y < 0 or new_y >= ROW:
            continue
        if maps[new_y][new_x] != 1:
            continue
        if answer[new_y][new_x] > 0:
            continue
        answer[new_y][new_x] = answer[y][x] + 1
        queue.append((new_x, new_y))

for i in range(ROW):
    for j in range(COLUMN):
        if answer[i][j] == 0 and maps[i][j] == 1:
            answer[i][j] = -1
        print(answer[i][j], end = ' ')
    print()