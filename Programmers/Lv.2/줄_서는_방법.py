import math

def solution(n, k):
    answer = []
    numbers = [(i + 1) for i in range(n)]
    case = [1 for _ in range(n)]
    
    for i in range(1, len(case)):
        case[i] = case[i] * case[i-1] * (i + 1)
        
    for i in range(len(case)-1, -1, -1):
        if k <= case[i]:
            answer.append(numbers.pop(math.ceil(k / case[i-1]) - 1))
            k = k % case[i-1]
        else:
            answer.append(numbers.pop(0))
        
    return answer