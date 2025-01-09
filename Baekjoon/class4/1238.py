# import sys
# import heapq
# input = sys.stdin.readline

# N, M, X = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# results = dict()

# def get_min_time(start, end):
#     visited = set()
#     times = [(0, start)]
#     heapq.heapify(times)
    
#     while times:
#         time, town = heapq.heappop(times)
#         if town == end:
#             return time
#         for next_town, next_time in graph[town]:
#             if (town, next_town) in visited:
#                 continue
#             visited.add((town, next_town))
#             heapq.heappush(times, (time + next_time, next_town))

#     return -1

# for _ in range(M):
#     start, end, time = map(int, input().split())
#     graph[start].append((end, time))

# for i in range(1, N+1):
#     if i == X:
#         continue
#     results[i] = get_min_time(i, X) + get_min_time(X, i)

# print(max(results.values()))

import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph1 = [[] for _ in range(N+1)] # 마을에서 X로 갈 때 사용
graph2 = [[] for _ in range(N+1)] # X에서 마을로 갈 때 사용

def dijkstra(start, graph):
    queue = []
    heapq.heappush(queue, (0, start))
    times = [int(1e9) for _ in range(N+1)]
    times[start] = 0

    while queue:
        time, town = heapq.heappop(queue)
        for next_town, next_time in graph[town]:
            if times[next_town] > time + next_time:
                times[next_town] = time + next_time
                heapq.heappush(queue, (time + next_time, next_town))

    return times[1:]

for _ in range(M):
    start, end, time = map(int, input().split())
    graph1[end].append((start, time))
    graph2[start].append((end, time))

print(max([t1+t2 for t1, t2 in zip(dijkstra(X, graph1), dijkstra(X, graph2))]))