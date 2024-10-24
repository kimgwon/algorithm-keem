import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(" "))
graph = defaultdict(list)
visited = set()
answer = 0

for _ in range(M):
    start, end = map(int, input().split(" "))
    graph[start].append(end)
    graph[end].append(start)

def check_graph(key):
    queue = deque([key])
    visited.add(key)
    while queue:
        key = queue.popleft()
        for node in graph[key]:
            if node not in visited:
                visited.add(node)
                queue.append(node)

for key in graph:
    if key not in visited:
        check_graph(key)
        answer += 1

print(answer + (N - len(visited)))