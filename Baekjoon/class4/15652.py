import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
values = [str(i) for i in range(1, N+1)]
result = ['0'] * M

def comb(depth, start):
    if depth >= M:
        print(' '.join(result))
        return    
    for i in range(start, N):
        result[depth] = values[i]
        comb(depth+1, i)

comb(0, 0)