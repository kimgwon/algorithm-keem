from itertools import combinations 

def solution(numbers, target):
    answer = 0
    
    for i in range(1, len(numbers)):
        comb = list(combinations(numbers, i))
        for c in comb:
            if sum(c)*2 == sum(numbers)-target:
                answer += 1
    
    return answer

# DFS 풀이
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# product 풀이
# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)