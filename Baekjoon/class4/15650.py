import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split(" "))
answer = combinations([str(i) for i in range(1, N+1)], M)

for a in sorted(answer):
    print(' '.join(a))