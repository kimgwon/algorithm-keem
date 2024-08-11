def solution(n):
    answer = []
    snail = [[0 for _ in range(i+1)] for i in range(n)]
    start, end = 1, sum([i for i in range(1, n+1)])
    i, j = 0, 0
    states = ["down", "right", "up"]
    state = states[0]
    current_round = 1
    
    while start <= end:
        snail[i][j] = start
        start += 1
        
        if state == states[0]:
            i += 1
            if i == n - current_round:
                state = states[1]
        elif state == states[1]:
            j += 1
            if j == len(snail[i]) - current_round:
                state = states[2]
        else:
            i -= 1
            j -= 1
            if i == current_round*2 - 1:
                state = states[0]
                current_round += 1
    
    for i in range(len(snail)):
        answer.extend(snail[i])
                
    return answer