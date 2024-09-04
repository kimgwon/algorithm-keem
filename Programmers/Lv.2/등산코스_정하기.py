import heapq
INF = int(1e9)
def solution(n, paths, gates, summits):
    answer = [INF, INF]
    
    graph = [[] for _ in range(n+1)]
    for i,j,w in paths:
        graph[i].append((w,j))
        graph[j].append((w,i))
        
    distance = [INF if i not in gates else 0 for i in range(n+1)]
    q = []
    
    gates = set(gates)
    summits = set(summits)
    
    for start in gates:
        heapq.heappush(q, (0, start))
        
    while q:
        cost, course = heapq.heappop(q)
        
        if course in summits:
            if cost < answer[1] or (cost == answer[1] and course < answer[0]):
                answer = [course, cost]
            continue
            
        if cost > distance[course]:
            continue

        for next_cost, next_course in graph[course]:
            if next_course in gates:
                continue

            next_distance = max(cost, next_cost)
            if distance[next_course] > max(cost, next_cost):
                distance[next_course] = next_distance
                heapq.heappush(q, (next_distance, next_course))

    return answer

# 시간 초과
# import heapq
# INF = int(1e9)
# def solution(n, paths, gates, summits):
#     answer = [INF, INF]
    
#     def dikjstra(summit, start):
#         nonlocal answer
        
#         graph = [[] for _ in range(n+1)]
#         for i,j,w in paths:
#             heapq.heappush(graph[i], (w,j))
#             heapq.heappush(graph[j], (w,i))
    
#         distance = [INF if i not in summits else 0 for i in range(n+1)]
        
#         q = []
#         heapq.heappush(q, (0, start))
        
#         while q:
#             cost, course = heapq.heappop(q)
#             if course in gates:
#                 if cost < answer[1] or (cost == answer[1] and summit < answer[0]):
#                     answer = [summit, cost]
#                 return
            
#             while graph[course]:
#                 next_cost, next_course = heapq.heappop(graph[course])
                
#                 if next_course in summits:
#                     continue
                    
#                 next_distance = max(cost, next_cost)
#                 if distance[next_course] > max(cost, next_cost):
#                     distance[next_course] = next_distance
#                     heapq.heappush(q, (next_distance, next_course))
            
            
#     for summit in summits:
#         dikjstra(summit, summit)
    
#     return answer
