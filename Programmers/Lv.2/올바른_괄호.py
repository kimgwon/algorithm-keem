from collections import deque

def solution(s):
    q = deque()
    for i in s:
        if i=='(':
            q.append(i)
        else:
            if q:
                q.popleft()
            else:
                return False
            
    return True if not q else False