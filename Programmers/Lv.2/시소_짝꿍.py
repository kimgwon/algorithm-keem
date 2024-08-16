from collections import Counter

def solution(weights):
    answer = 0
    weights = Counter(weights)
    
    for c in weights:
        answer += (weights[c] * (weights[c]-1)) // 2
        answer += (weights[c*3/2] + weights[c*4/2] + weights[c*4/3]) * weights[c]
    
    return answer