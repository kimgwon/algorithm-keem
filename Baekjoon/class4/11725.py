import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
tree = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]
parent[0] = 1
parent[1] = 1
queue = deque([1])

for _ in range(N - 1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)

while queue:
    node = queue.popleft()
    for i in tree[node]:
        if parent[i] == 0:
            parent[i] = node
            queue.append(i)

for i in range(2, N+1):
    print(parent[i])