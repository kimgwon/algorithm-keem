import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [(0,1),(0,-1),(1,0),(-1,0)]

answer = 1
max_k = 0
for g in graph:
    for i in g:
        max_k = max(max_k, i)

def bfs(x, y, visited, k):
    result = 0
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        result += 1
        
        for dx, dy in move:
            new_x = x + dx
            new_y = y + dy

            if new_x<0 or new_x>=n or new_y<0 or new_y>=n:
                continue

            if visited[new_y][new_x] or graph[new_y][new_x] <= k:
                continue

            visited[new_y][new_x] = True
            q.append((new_x, new_y))
    return result

for k in range(1, max_k+1):
    result = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] or graph[i][j] <= k:
                continue
            visited[i][j] = True
            if bfs(j,i,visited,k):
                result += 1
    answer = max(answer, result)

print(answer)