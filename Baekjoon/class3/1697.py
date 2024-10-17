import sys
from collections import deque
MIN_VALUE = 0
MAX_VALUE = 100000
input = sys.stdin.readline

N, K = map(int, input().split(" "))

def bfs(N):
    queue = deque()
    visited = set()
    queue.append((N, 0))

    while queue:
        N, time = queue.popleft()
        if N == K:
            return time
            
        if N - 1 not in visited and N - 1 >= MIN_VALUE:
            queue.append((N - 1, time + 1))
            visited.add(N - 1)
        if N + 1 not in visited and N + 1 <= MAX_VALUE:
            queue.append((N + 1, time + 1))
            visited.add(N + 1)
        if N * 2 not in visited and N * 2 <= MAX_VALUE * 2:
            queue.append((N * 2, time + 1))
            visited.add(N * 2)

if N >= K:
    print(N - K)
else:
    print(bfs(N))