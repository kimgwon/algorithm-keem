from itertools import combinations 

def solution(numbers, target):
    answer = 0
    
    for i in range(1, len(numbers)):
        comb = list(combinations(numbers, i))
        for c in comb:
            if sum(c)*2 == sum(numbers)-target:
                answer += 1
    
    return answer