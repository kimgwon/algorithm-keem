from collections import deque

def solution(queue1, queue2):
    answer = 0
    max_cnt = len(queue1) + len(queue2) + 1
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    
    while sum_queue1 != sum_queue2:    
        if answer > max_cnt:
            return -1
        
        if sum_queue1 > sum_queue2:
            queue2.append(queue1.popleft())
            sum_queue1 -= queue2[-1]
            sum_queue2 += queue2[-1]
        elif sum_queue1 < sum_queue2:
            queue1.append(queue2.popleft())
            sum_queue1 += queue1[-1]
            sum_queue2 -= queue1[-1]
        answer += 1
    
    return answer