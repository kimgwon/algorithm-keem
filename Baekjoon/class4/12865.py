# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# items = [tuple(map(int, input().split())) for _ in range(N)]
# bag = [[0 for _ in range(K+1)] for _ in range(N+1)]

# for i in range(1, N+1):
#     for j in range(1, K+1):
#         item = items[i-1]
#         if item[0] <= j:
#             bag[i][j] = max(item[1] + bag[i-1][j-item[0]], bag[i-1][j])
#         else:
#             bag[i][j] = bag[i-1][j]

# print(bag[-1][-1])

# 개선
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
bag = { 0: 0 }

for w, v in items:
    temp = {}
    for bv, bw in bag.items():
        if bag.get(nv:=v+bv, K+1) > (nw:=w+bw):
            temp[nv] = nw
    bag.update(temp)

print(max(bag.keys()))