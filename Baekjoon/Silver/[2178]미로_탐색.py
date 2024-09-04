import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[int(r) for r in input().rstrip()] for _ in range(n)]

move = [(0,1),(0,-1),(1,0),(-1,0)]
visited = [[False for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0,0))

while q:
    x, y = q.popleft()
    for dx, dy in move:
        new_x = x+dx
        new_y = y+dy

        if new_x>=m or new_x<0 or new_y>=n or new_y<0:
            continue
        if not graph[new_y][new_x]:
            continue

        if not visited[new_y][new_x] or graph[y][x] + 1 < graph[new_y][new_x]:
            graph[new_y][new_x] = graph[y][x] + 1
            visited[new_y][new_x] = True
            q.append((new_x, new_y))

print(graph[n-1][m-1])