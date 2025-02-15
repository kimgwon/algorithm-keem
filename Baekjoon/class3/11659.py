import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
sums = [0] + nums.copy()

for i in range(2, len(nums)+1):
    sums[i] = sums[i-1] + nums[i-1]

for _ in range(M):
    i, j = map(int, input().split(' '))
    print(sums[j] - sums[i - 1])