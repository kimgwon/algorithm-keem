# 4:41
# 4:53
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]
answer = 0

for _ in range(M):
    i, j = map(int, input().split(' '))
    graph[i-1].append(j-1)
    graph[j-1].append(i-1)

queue = deque([0])
visited[0] = True
while queue:
    computer = queue.popleft()
    for next_computer in graph[computer]:
        if visited[next_computer]:
            continue
        visited[next_computer] = True
        queue.append(next_computer)

print(sum(visited) - 1)