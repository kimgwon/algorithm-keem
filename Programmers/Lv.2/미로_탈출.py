from collections import deque

def solution(maps):
    visited = [[0 for _ in maps[i]] for i in range(len(maps))]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    start_x, start_y = 0, 0
    lever_x, lerver_y = 0, 0
    end_x, end_y = 0, 0
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                start_x, start_y = j, i
            elif maps[i][j] == "L":
                lever_x, lever_y = j, i
            elif maps[i][j] == "E":
                end_x, end_y = j, i
                
    def bfs(from_x, from_y, to_x, to_y):
        queue = deque()
        queue.append((from_x, from_y))
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
            
                if new_x < 0 or new_x >= len(maps[0]) or new_y < 0 or new_y >= len(maps):
                    continue
                    
                if maps[new_y][new_x] == 'X':
                    continue

                if visited[new_y][new_x] == 0 or visited[new_y][new_x] > visited[y][x] + 1:
                    visited[new_y][new_x] = visited[y][x] + 1
                else:
                    continue

                if new_x == to_x and new_y == to_y:
                    break
                    
                queue.append((new_x, new_y))

    bfs(start_x, start_y, lever_x, lever_y)
    
    if visited[lever_y][lever_x] <= 0:
        return -1
    
    lever_degree = visited[lever_y][lever_x]
    
    visited = [[0 for _ in maps[i]] for i in range(len(maps))]
    bfs(lever_x, lever_y, end_x, end_y)
    
    return lever_degree + visited[end_y][end_x] if visited[end_y][end_x] else -1