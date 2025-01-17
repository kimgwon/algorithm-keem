import sys
input = sys.stdin.readline

n = int(input())

factorial = {0: 0, 1: 1, 2: 1}
def solution(n):
    if n in factorial:
        return factorial[n]
    if n % 2:
        a = solution(n//2 + 1)
        b = solution(n//2)
        factorial[n] = (a * a + b * b) % 1000000007
        return factorial[n]
    a = solution(n//2 + 1)
    b = solution(n//2 - 1)
    factorial[n] = (a * a - b * b) % 1000000007
    return factorial[n]

print(solution(n))