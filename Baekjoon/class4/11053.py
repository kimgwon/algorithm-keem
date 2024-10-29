import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split(" ")))
dp = [1 for _ in range(N)]

for i in range(1, len(nums)):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))