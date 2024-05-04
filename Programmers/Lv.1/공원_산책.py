def solution(park, routes):
    op = {'E': (1, 0), 'W': (-1, 0), 'S': (0, 1), 'N': (0, -1)}
    x, y = 0, 0
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = j, i
                break
                
    for route in routes:
        key, distance = route.split(' ')
        dx, dy = op[key]
        new_x, new_y = x, y
        is_move = True
        
        for d in range((int(distance))):
            new_x += dx
            new_y += dy
            
            if new_x < 0 or new_x >= len(park[0]) or new_y < 0 or new_y >= len(park) or park[new_y][new_x] == 'X':
                is_move = False
                break
            
        if is_move:
            x, y = new_x, new_y
            
    return [y,x]