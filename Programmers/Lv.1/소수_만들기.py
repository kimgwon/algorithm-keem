from itertools import combinations

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def solution(nums):
    answer = 0
    
    comb_nums = list(combinations(nums,3))
    for c in comb_nums:
        if is_prime(sum(c)):
            answer+=1
    
    return answer

# 소수 판정법: 주어진 자연수 n에 대해서 1보다 크고 루트 n 이하인 모든 자연수들로 나누어떨어지지 않으면 소수
# for i in range(2, int(x**0.5)+1):
#   if x%i==0:
#       answer+=1
