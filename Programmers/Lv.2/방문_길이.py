def solution(dirs):
    answer = 0
    x, y = 0, 0
    dx = {'U':0, 'D':0, 'R':1, 'L':-1}
    dy = {'U':1, 'D':-1, 'R':0, 'L':0}
    visited_x = [[False for _ in range(10)] for _ in range(11)]
    visited_y = [[False for _ in range(10)] for _ in range(11)]
    
    for d in dirs:
        new_x = x + dx[d]
        new_y = y + dy[d]
        
        if new_x>5 or new_x<-5 or new_y>5 or new_y<-5:
            continue
        
        if x == new_x:
            y = min(y, new_y)
            if not visited_y[x+5][y+5]:
                visited_y[x+5][y+5] = True
                answer += 1
        else:
            x = min(x, new_x)
            if not visited_x[y+5][x+5]:
                visited_x[y+5][x+5] = True
                answer += 1
        
        x,y = new_x, new_y
    
    return answer


# set을 이용하면 중복 관리가 알아서 된다..
# def solution(dirs):
#     answer = 0
#     x, y = 0, 0
#     dx = {'U': 0, 'D': 0, 'R': 1, 'L': -1}
#     dy = {'U': 1, 'D': -1, 'R': 0, 'L': 0}
    
#     visited = set()  # 경로를 저장할 set
    
#     for d in dirs:
#         new_x = x + dx[d]
#         new_y = y + dy[d]
        
#         # 좌표가 경계를 넘어가면 무시
#         if new_x > 5 or new_x < -5 or new_y > 5 or new_y < -5:
#             continue
        
#         # 경로를 양방향으로 저장
#         if ((x, y), (new_x, new_y)) not in visited:
#             visited.add(((x, y), (new_x, new_y)))
#             visited.add(((new_x, new_y), (x, y)))  # 반대 방향 경로도 추가
#             answer += 1
        
#         # 좌표 업데이트
#         x, y = new_x, new_y
    
#     return answer
