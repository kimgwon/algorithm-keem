# dfs는 효율성 0점
# import sys
# sys.setrecursionlimit(10**7)

# def solution(maps):
#     ROW, COL = len(maps[0]), len(maps)
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
    
#     def dfs(x, y):
#         for i in range(4):
#             new_x = x + dx[i]
#             new_y = y + dy[i]
            
#             if new_x<0 or new_x>=ROW or new_y<0 or new_y>=COL:
#                 continue
#             if (new_x == 0 and new_y == 0) or maps[new_y][new_x] == 0:
#                 continue
            
#             if maps[new_y][new_x] == 1 or maps[new_y][new_x] > maps[y][x] + 1:
#                 maps[new_y][new_x] = maps[y][x] + 1
#                 dfs(new_x, new_y)
            
#     dfs(0,0)
    
#     return maps[COL-1][ROW-1] if maps[COL-1][ROW-1] != 1 else -1


import sys
from collections import deque
sys.setrecursionlimit(10**7)

def solution(maps):
    ROW, COL = len(maps[0]), len(maps)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if new_x<0 or new_x>=ROW or new_y<0 or new_y>=COL:
                continue
            if (new_x == 0 and new_y == 0) or maps[new_y][new_x] == 0:
                continue
            
            if maps[new_y][new_x] == 1 or maps[new_y][new_x] > maps[y][x] + 1:
                maps[new_y][new_x] = maps[y][x] + 1
                queue.append((new_x, new_y))
    
    return maps[COL-1][ROW-1] if maps[COL-1][ROW-1] != 1 else -1