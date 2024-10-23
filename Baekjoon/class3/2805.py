import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))
trees.sort()

left, right = 0, trees[-1]
answer = 0
while left <= right:
    result = 0
    mid = (left + right) // 2
    for tree in trees:
        if tree >= mid:
            result += (tree - mid)

    if result >= M:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
print(answer)