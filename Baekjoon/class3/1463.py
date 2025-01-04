import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
visited = { N }
queue = deque([(N, 0)])

while queue:
    num, cnt = queue.popleft()
    if num == 1:
        print(cnt)
        break
    elif num < 1:
        continue
    
    if num % 3 == 0  and num // 3 not in visited:
        visited.add(num//3)
        queue.append((num//3, cnt+1))
    if num % 2 == 0 and num // 2 not in visited:
        visited.add(num//2)
        queue.append((num//2, cnt+1))
    if num - 1 not in visited:
        visited.add(num - 1)
        queue.append((num-1, cnt+1))
    