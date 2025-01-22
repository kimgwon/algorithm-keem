# import sys
# from collections import deque
# input = sys.stdin.readline

# A, B = map(int, input().split())
# queue = deque([(A, 1)])

# while queue:
#     x, cnt = queue.popleft()
#     if x > B:
#         continue
#     elif x == B:
#         print(cnt)
#         break

#     queue.append((x * 2, cnt + 1))
#     queue.append((x * 10 + 1, cnt + 1))
# else:
#     print(-1)

import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1

while A <= B:
    if A == B:
        print(cnt)
        break
    if B % 10 == 1: B//=10
    elif B % 2 == 0: B//=2
    else: 
        print(-1) 
        break
    cnt += 1
else:
    print(-1)