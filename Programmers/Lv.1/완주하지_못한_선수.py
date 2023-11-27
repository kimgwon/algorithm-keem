from collections import deque

def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    completion = deque(completion)
    
    for p in participant:
        if not completion:
            answer = p
            break
            
        if p == completion[0]:
            completion.popleft()
        else:
            answer = p
            break
    
    return answer