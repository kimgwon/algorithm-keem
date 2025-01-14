# import sys
# input = sys.stdin.readline

# A, B, C = map(int, input().split())
# result = 1
# while B >= 1:
#     if B % 2:
#         result = (result * A) % C
#     A %= C
#     A = A * A % C
#     B //= 2
# print(result)

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def solution(A, B, C):
    if B == 1:
        return A % C
    result = solution(A, B//2, C)
    if B % 2:
        return (result * result * A) % C
    return (result * result) % C

print(solution(A, B, C))