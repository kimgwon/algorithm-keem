import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
empties = []
move = [(0,1),(0,-1),(1,0),(-1,0)]
answer = n*m

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 0:
            empties.append((i,j))
    graph.append(line)

def bfs(row, col):
    q = deque([])
    q.append((col, row))
    result = 0
    while q:
        x, y = q.popleft()

        if result > answer:
            return result

        for dx, dy in move:
            new_x, new_y = x + dx, y + dy

            if new_x<0 or new_x>=m or new_y<0 or new_y>=n:
                continue

            if visited[new_y][new_x] or graph[new_y][new_x] == 1:
                continue
            elif graph[new_y][new_x] == 0:
                result += 1

            visited[new_y][new_x] = True
            q.append((new_x, new_y))

    return result

for w1, w2, w3 in combinations(empties, 3):
    visited = [[False for _ in range(m)] for _ in range(n)]
    result = 0
    graph[w1[0]][w1[1]] = 1
    graph[w2[0]][w2[1]] = 1
    graph[w3[0]][w3[1]] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 2:
                continue
            visited[i][j] = True
            result += bfs(i,j)
    answer = min(answer, result)
    graph[w1[0]][w1[1]] = 0
    graph[w2[0]][w2[1]] = 0
    graph[w3[0]][w3[1]] = 0

print(len(empties) - answer - 3)