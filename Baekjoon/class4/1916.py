import sys
import heapq
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(int(input())):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())
costs = [(0, start)]
visited = [int(1e9) for _ in range(N+1)]
while costs:
    now_cost, now_city = heapq.heappop(costs)
    if now_city == end:
        print(now_cost)
        break
    for next_city, next_cost in graph[now_city]:
        if visited[next_city] <= now_cost + next_cost:
            continue
        visited[next_city] = now_cost + next_cost
        heapq.heappush(costs, (now_cost + next_cost, next_city))