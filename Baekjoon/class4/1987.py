# import sys
# input = sys.stdin.readline

# R, C = map(int, input().split(" "))
# graph = [[col for col in input().rstrip()] for row in range(R)]
# visited = [False] * 26
# move = [(0,1), (0,-1), (1,0), (-1,0)]
# answer = 1

# def dfs(x, y, cnt):
#     global answer
#     answer = max(answer, cnt)
#     for dx, dy in move:
#         new_x = x + dx
#         new_y = y + dy
#         if new_x < 0 or new_x >= C or new_y < 0 or new_y >= R:
#             continue
#         if visited[ord(graph[new_y][new_x]) - ord('A')]:
#             continue
#         visited[ord(graph[new_y][new_x]) - ord('A')] = True
#         dfs(new_x, new_y, cnt + 1)
#         visited[ord(graph[new_y][new_x]) - ord('A')] = False

# visited[ord(graph[0][0]) - ord('A')] = True
# dfs(0, 0, 1)
# print(answer)

import sys
input = sys.stdin.readline

R, C = map(int, input().split(" "))
graph = [[col for col in input().rstrip()] for row in range(R)]
move = [(0,1), (0,-1), (1,0), (-1,0)]

def dfs(x, y):
    answer = 1
    stack = set()
    stack.add((x, y, graph[y][x]))
    while stack:
        x, y, visited = stack.pop()
        answer = max(answer, len(visited))
        for dx, dy in move:
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_x >= C or new_y < 0 or new_y >= R:
                continue
            if graph[new_y][new_x] in visited:
                continue
            stack.add((new_x, new_y, visited + graph[new_y][new_x]))
    return answer

print(dfs(0, 0))