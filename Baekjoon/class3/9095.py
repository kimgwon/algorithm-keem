import sys
from collections import deque
input= sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    queue = deque([0])
    cnt = 0
    while queue:
        x = queue.popleft()
        if x == n:
            cnt += 1
            continue
        if x + 1 <= n:
            queue.append(x + 1)
        if x + 2 <= n:
            queue.append(x + 2)
        if x + 3 <= n:
            queue.append(x + 3)
    print(cnt)