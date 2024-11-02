import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().strip())
tree = defaultdict(set)
result = [0 for _ in range(N)]

for _ in range(N - 1):
    i, j = map(int, input().split())
    tree[i].add(j)
    tree[j].add(i)

result[0] = 1
stack = []
