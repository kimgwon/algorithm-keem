import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))

answer = 300001

for comb in combinations(cards, 3):
    result = sum(comb)
    if result > M:
        continue
    answer = min(answer, M - result)

print(M - answer)