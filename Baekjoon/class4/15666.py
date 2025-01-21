import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
result = [0] * M

def comb(depth, start):
    if depth >= M:
        print(' '.join([str(i) for i in result]))
        return
    for i in range(start, len(nums)):
        result[depth] = nums[i]
        comb(depth+1, i)

comb(0, 0)