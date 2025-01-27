# import sys
# from collections import deque
# from itertools import combinations
# input = sys.stdin.readline

# N, M = map(int, input().split())
# roads = [list(map(int, input().split())) for _ in range(N)]
# moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# chickens = []
# homes = dict()
# city_degree = int(1e9)

# def bfs(home, cnt_chickens):
#     global roads, homes
#     queue = deque([(home, 0)])
#     visited = [[False for _ in range(N)] for _ in range(N)]
    
#     while queue and cnt_chickens:
#         (x, y), degree = queue.popleft()
#         if roads[x][y] == 2:
#             homes[home].append((degree, (x, y)))
#             cnt_chickens -= 1
#         for dx, dy in moves:
#             new_x, new_y = x + dx, y + dy
#             if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
#                 continue
#             if visited[new_x][new_y]:
#                 continue
#             visited[new_x][new_y] = True
#             queue.append(((new_x, new_y), degree + 1))
#     return -1

# # 치킨 거리 저장할 딕셔너리 생성
# for i in range(len(roads)):
#     for j in range(len(roads[i])):
#         if roads[i][j] == 1:
#             homes[(i, j)] = list()
#         elif roads[i][j] == 2:
#             chickens.append((i, j))

# for home in homes:
#     bfs(home, len(chickens))

# # 사라질 치킨 집 구하기
# for remove_chickens in combinations(chickens, (len(chickens) - M)):
#     temp_city_degree = 0

#     for home in homes:
#         if temp_city_degree >= city_degree: break
#         for degree, chicken in homes[home]:
#             if chicken not in remove_chickens:
#                 temp_city_degree += degree
#                 break

#     city_degree = min(city_degree, temp_city_degree)

# print(city_degree)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(N)]
homes = []
chickens = []
city_degree = int(1e9)

def get_chicken_dist(selected_chickens):
    total_dist = 0
    for hx, hy in homes:
        min_dist = int(1e9)
        for cx, cy in selected_chickens:
            min_dist = min(min_dist, abs(hx-cx) + abs(hy-cy))
        total_dist += min_dist
    return total_dist

def bt(depth, selected_chickens):
    global city_degree
    if len(selected_chickens) == M:
        city_degree = min(city_degree, get_chicken_dist(selected_chickens))
        return city_degree
    for i in range(depth, len(chickens)):
        selected_chickens.append(chickens[i])
        bt(i+1, selected_chickens)
        selected_chickens.pop()
    return city_degree

# 치킨 거리 저장할 딕셔너리 생성
for i in range(len(roads)):
    for j in range(len(roads[i])):
        if roads[i][j] == 1:
            homes.append((i, j))
        elif roads[i][j] == 2:
            chickens.append((i, j))

print(bt(0, []))