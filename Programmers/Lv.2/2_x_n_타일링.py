# dict에 넣을 때 나머지 계산 안해주면 시간초과 남 띠용;
import sys
sys.setrecursionlimit(10**7)

def solution(n):
    case_dict = {}
    
    def case(x):
        if (x==n):
            return 1
        elif x<n:
            if x not in case_dict:
                case_dict[x] = (case(x+1) + case(x+2)) % 1000000007
            return case_dict[x]
        else:
            return 0
    
    return (case(1) + case(2)) % 1000000007

# 함수 호출 안하는 방식 DP
def solution(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, (a + b) % 1000000007
    return b

######
# 시간 초과
from itertools import combinations

def solution(n):
    answer = 0
    
    def nCr(n,r):
        n1, r1 = 1, 1
        for i in range(r):
            n1 *= (n-i)
        for i in range(1, r+1):
            r1 *= i
        return n1//r1
    
    for i in range(n - n//2 + (n-1)%2) :
        answer += nCr(n-i, i)
        
    return answer

# 시간 초과
def solution(n):
    def possible(x):
        if (x==n):
            return 1
        elif (x<n):
            return possible(x+1) + possible(x+2)
        else:
            return 0
        
    return possible(1) + possible(2)