# import sys
# sys.setrecursionlimit(10**7)
# input = sys.stdin.readline

# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# move = [(1,0), (1,-1), (1,1)]

# def dfs(TYPE):
#     memo = [[-1 if TYPE == "max" else int(1e9) for _ in range(3)] for _ in range(N)]
#     for i in range(3):
#         memo[0][i] = graph[0][i]
#     stack = [(0, 0), (0, 1), (0, 2)]
#     while stack:
#         x, y = stack.pop()
#         for dx, dy in move:
#             new_x, new_y = x + dx, y + dy
#             if new_x < 0 or new_x >= N or new_y < 0 or new_y >= 3:
#                 continue
#             if TYPE == "max" and memo[new_x][new_y] >= memo[x][y] + graph[new_x][new_y]:
#                 continue
#             elif TYPE == "min" and memo[new_x][new_y] <= memo[x][y] + graph[new_x][new_y]:
#                  continue
#             memo[new_x][new_y] = memo[x][y] + graph[new_x][new_y]
#             stack.append((new_x, new_y))
#     return max(memo[-1]) if TYPE == "max" else min(memo[-1])

# print(dfs("max"), dfs("min"))

import sys
input = sys.stdin.readline

N = int(input())
graph = [[i, i] for i in map(int, input().split())]
next_graph = [-1] * 3
memo = [[-1, int(1e9)] for _ in range(3)]
move = [0, -1, 1]

for _ in range(N-1):
    next_graph[0], next_graph[1], next_graph[2] = map(int, input().split())
    for i in range(3):
        memo[i][0], memo[i][1] = -1, int(1e9)
    for i in range(3):
        for di in move:
            new_i = i + di
            if new_i < 0 or new_i >= 3:
                continue
            memo[new_i][0], memo[new_i][1] = max(memo[new_i][0], graph[i][0] + next_graph[new_i]), min(memo[new_i][1], graph[i][1] + next_graph[new_i])
    for i in range(3):
        graph[i][0], graph[i][1] = memo[i][0], memo[i][1]

print(max([i for i, _ in graph]), min([j for _, j in graph]))