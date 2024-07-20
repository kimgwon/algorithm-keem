from collections import deque

def solution(msg):
    answer = []
    msg = deque(msg)
    lzw = {chr(ord('A') + i) : i+1 for i in range(26)}
    
    while msg:
        w = msg.popleft()
        while msg:
            s = msg[0]
            if w+s not in lzw:
                lzw[w+s] = len(lzw) + 1
                break
            msg.popleft()
            w += s
        answer.append(lzw[w])
        
    return answer