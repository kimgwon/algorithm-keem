def solution(number, k):
    answer = []
    
    for i in range(len(number)):
        if not answer:
            answer.append(number[i])
            continue
        
        while answer and k:
            if answer[-1] < number[i]:
                answer.pop()
                k -= 1
            else:
                break
                
        answer.append(number[i])
    
    return ''.join(answer) if not k else ''.join(answer[:-k])