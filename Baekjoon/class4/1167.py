# 21:49

# import sys
# import heapq
# input = sys.stdin.readline

# V = int(input())
# graph = [[] for _ in range(V+1)]

# def dijkstra(start):
#     dist = [0 for _ in range(V+1)]
#     queue = [(0, start)]
#     while queue:
#         cost, node = heapq.heappop(queue)
#         for n_node, n_cost in graph[node]:
#             if dist[n_node] == 0 or dist[n_node] < cost - n_cost:
#                 dist[n_node] = cost - n_cost
#                 queue.append((cost - n_cost, n_node))

#     return -min(dist)

# for _ in range(V):
#     node = list(map(int, input().split()))
#     for i in range(1, len(node), 2):
#         if node[i] == -1:
#             break
#         graph[node[0]].append((node[i], node[i+1]))

# result = 0
# for i in range(V):
#     result = max(result, dijkstra(i))
# print(result)

import sys
import heapq
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]

def dfs(start):
    dist = [0 for _ in range(V+1)]
    stack = [(0, start)]
    while stack:
        cost, node = stack.pop()
        for n_node, n_cost in graph[node]:
            if n_node == start:
                continue
            if dist[n_node] == 0 or dist[n_node] < cost - n_cost:
                dist[n_node] = cost - n_cost
                stack.append((cost - n_cost, n_node))
    return dist

for _ in range(V):
    node = list(map(int, input().split()))
    for i in range(1, len(node), 2):
        if node[i] == -1:
            break
        graph[node[0]].append((node[i], node[i+1]))

result = dfs(1)
print(-min(dfs(result.index(min(result)))))