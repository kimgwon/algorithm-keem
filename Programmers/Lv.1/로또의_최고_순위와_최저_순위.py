def solution(lottos, win_nums):
    answer = 0
    temp = 0
    
    for win_num in win_nums:
        if win_num not in lottos:
            temp+=1
        else:
            answer+=1
            
    possible = min(lottos.count(0), temp)
    
    if answer+possible==0:
        return [6,6]
            
    return [7-(answer+possible), min(6,7-answer)]