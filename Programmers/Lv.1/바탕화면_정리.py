def solution(wallpaper):
    answer = [51, 51, 0, 0]
    
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[y])):
            if wallpaper[y][x] == '.':
                continue
            answer = [min(answer[0], y), min(answer[1], x)
                      , max(answer[2], y+1), max(answer[3], x+1)]
    return answer