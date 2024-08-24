def solution(places):
    move = [(0,-1), (0,1), (-1,0), (1,0)]
    
    # PP, POP, PO - P
    def checkDistance(place):
        for i in range(5):
            for j in range(5):
                cnt = 0
                if place[i][j] == 'P':
                    for dx, dy in move:
                        new_x, new_y = j + dx, i + dy
                        if new_x<0 or new_x>=5 or new_y<0 or new_y>=5:
                            continue
                        if place[new_y][new_x] == 'P':
                            return 0
                elif place[i][j] == 'O':
                    for dx, dy in move:
                        new_x, new_y = j + dx, i + dy
                        if new_x<0 or new_x>=5 or new_y<0 or new_y>=5:
                            continue
                        if place[new_y][new_x] == 'P':
                            cnt += 1
                    if cnt >= 2:
                        return 0
        return 1
        
    return [checkDistance(place) for place in places]