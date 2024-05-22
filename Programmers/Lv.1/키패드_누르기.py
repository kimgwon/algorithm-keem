# numbers 반복문
# 1,4,7 -> L
# 3,6,9 -> R
# 2,5,8,0 -> 가까운 엄지, 같으면 hand
# 2,5,8 이면 차이가 적은 수
# 0이면 큰 수
from collections import deque

def bfs(x, y, to_x, to_y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    move = [[0 for _ in range(3)] for _ in range(4)]
    queue = deque([(x,y)])
    
    if x == to_x and y == to_y:
        return 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x<0 or new_x>2 or new_y<0 or new_y>3:
                continue

            if move[new_y][new_x] == 0 or move[new_y][new_x] > move[y][x] + 1:
                move[new_y][new_x] = move[y][x] + 1
                queue.append((new_x, new_y))

    return move[to_y][to_x]
    
def solution(numbers, hand):
    answer = ''
    # 0~9 좌표
    xy = [(1,3)]
    xy.extend([(x, y) for y in range(3) for x in range(3)])
    l_xy = (0, 3)
    r_xy = (2, 3)
    use_l = [1, 4, 7]
    use_r = [3, 6, 9]
    
    for number in numbers:
        if number in use_l:
            l_xy = xy[number]
            answer += "L"
        elif number in use_r:
            r_xy = xy[number]
            answer += "R"
        else:
            l = bfs(l_xy[0], l_xy[1], xy[number][0], xy[number][1])
            r = bfs(r_xy[0], r_xy[1], xy[number][0], xy[number][1])
            
            if l<r or (l==r and hand == "left"):
                l_xy = xy[number]
                answer += "L"
            else:
                r_xy = xy[number]
                answer += "R"
            
    return answer