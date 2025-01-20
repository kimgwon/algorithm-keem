import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    result = [[j for j in stickers[i]] for i in range(2)]

    for i in range(1, n):
        if i == 1:
            result[0][i] += result[1][i-1]
            result[1][i] += result[0][i-1]
        else: # 이전에 스티커를 떼지 않았을 경우와 떼었을 경우
            before = max(result[0][i-2], result[1][i-2])
            result[0][i] += max(before, result[1][i-1])
            result[1][i] += max(before, result[0][i-1])
    
    print(max(result[0][-1], result[1][-1]))