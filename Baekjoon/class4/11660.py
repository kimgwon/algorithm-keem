# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# nums = [list(map(int, input().split())) for _ in range(N)]
# prefix = [[0 for _ in range(N)] for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         prefix[i][j] = nums[i][j]
#         if i > 0:
#             prefix[i][j] += prefix[i-1][j]
#         if j > 0:
#             prefix[i][j] += prefix[i][j-1]
#         if i > 0 and j > 0:
#             prefix[i][j] -= prefix[i-1][j-1]

# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     result = prefix[x2-1][y2-1]
#     if x1 > 1:
#         result -= prefix[x1-2][y2-1]
#     if y1 > 1:
#         result -= prefix[x2-1][y1-2]
#     if x1 > 1 and y1 > 1:
#         result += prefix[x1-2][y1-2]
#     print(result)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
prefix = [[0] * (N + 1) for _ in range(N + 1)]  # (N+1)x(N+1)로 확장

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = nums[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
    print(result)