import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = map(int, input().split())

for p in sorted(set(permutations(nums, M))):
    print(*p)