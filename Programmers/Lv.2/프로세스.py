from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = [(priorities[idx], idx==location) for idx in range(len(priorities))]
    priorities = deque(priorities)
    
    while priorities:
        max_priority = max(priorities)
        priority = priorities.popleft()
        
        if priority[0] == max_priority[0]:
            answer += 1
            if priority[1]:
                return answer
        else:
            priorities.append(priority)
    
    return answer