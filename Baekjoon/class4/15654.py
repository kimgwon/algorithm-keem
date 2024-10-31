import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split(" "))
nums = sorted(list(map(int, input().split(" "))))

for comb in list(combinations(nums, M)):
    print(comb)