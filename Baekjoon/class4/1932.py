import sys
import math
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split(" "))) for _ in range(n)]

for i in range(1, n):
    nums[i][0] += nums[i-1][0]
    nums[i][-1] += nums[i-1][-1]
    for j in range(1, len(nums[i])-1):
        nums[i][j] = max(nums[i-1][j-1] + nums[i][j], nums[i-1][j] + nums[i][j])

print(math.factorial(500))
print(max(nums[-1]))