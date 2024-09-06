import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[int(i) for i in input().rstrip()] for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for i in range(N)]
move = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(x, y):
    q = deque([])
    q.append((x, y, False))

    while q:
        x, y, is_broken = q.popleft()
        if x == M-1 and y == N-1:
            return visited[y][x][is_broken] + 1

        for dx, dy in move:
            new_x = dx+x
            new_y = dy+y

            if new_x<0 or new_x>=M or new_y<0 or new_y>=N:
                continue
            # 벽이라면
            if graph[new_y][new_x]:
                # 1. 벽을 부신적이 없을 때 2. 해당 길을 간 적이 없을 때
                # 이동한다.
                if not is_broken and not visited[new_y][new_x][True]:
                    visited[new_y][new_x][True] = visited[y][x][False] + 1
                    q.append((new_x,new_y,True))
            # 벽이 아니라면
            else:
                # 1. (부신적이 있든 없든) 해당 길을 간 적이 없을 때
                # 이동한다.
                if not visited[new_y][new_x][is_broken]:
                    visited[new_y][new_x][is_broken] = visited[y][x][is_broken] + 1
                    q.append((new_x,new_y,is_broken))
    return -1

print(bfs(0,0))