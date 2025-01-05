# 1. 세로로 넣는다 -> 1칸
# 2. 가로로 넣는다 -> 2칸
# 하향식
import sys
input = sys.stdin.readline

dic = { 1: 1, 2: 2 }

def solution(n):
    if n < 0:
        return 0
    elif n in dic:
        return dic[n]
    dic[n] = (solution(n-1) + solution(n-2)) % 10007
    return dic[n]

print(solution(int(input())))

# 상향식
# dp[i]는 dp[i-1]의 뒤에 세로 나무를 놓은 것과, dp[i-2]의 뒤에 가로 나무를 놓은 것의 합과 같다.
# n = int(input())
# dp = [0, 1, 2]
# for i in range(3, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
# print(dp[n])