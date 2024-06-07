# import sys
# sys.setrecursionlimit(10**7)

# def solution(n):
#     fib_dict = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5}
    
#     def fib(n):
#         if n in fib_dict:
#             return fib_dict[n]
#         fib_dict[n] = fib(n-2) + fib(n-1)
#         return fib_dict[n]
    
#     return fib(n) % 1234567

# sys 모듈을 통해 재귀의 한도를 늘려준다.

# 피보나치 재귀로 안푸는 방법
def solution(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        
    return a % 1234567