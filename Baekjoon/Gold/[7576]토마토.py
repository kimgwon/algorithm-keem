import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
graph = []
tomatos = deque([])
move = [(0,1),(0,-1),(1,0),(-1,0)]
answer = 0

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 1:
            tomatos.append((i,j))
    graph.append(line)

while tomatos:
    row, col = tomatos.popleft()
    for dr, dc in move:
        new_row = row + dr
        new_col = col + dc
        if new_row < 0 or new_row >= N or new_col < 0 or new_col >= M:
            continue
        if graph[new_row][new_col] == -1:
            continue
        if not graph[new_row][new_col]:
            graph[new_row][new_col] = graph[row][col]+1
            tomatos.append((new_row, new_col))

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 0:
            print(-1)
            exit()
        answer = max(answer, graph[i][j]-1)

print(answer)