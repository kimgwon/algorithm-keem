from collections import deque

def solution(order):
    answer = 0
    boxes = deque([i for i in range(1, len(order)+1)]) # 큐
    sub = [] # 스택
    idx = 0
    
    while boxes or sub:
        if  idx >= len(order):
            break
        if boxes and boxes[0] == order[idx]:
            boxes.popleft()
            idx += 1
            answer += 1
        elif sub and sub[-1] == order[idx]:
            sub.pop()
            idx += 1
            answer += 1
        elif boxes:
            sub.append(boxes.popleft())
        else:
            break
            
    return answer