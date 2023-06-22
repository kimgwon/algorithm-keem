def solution(dartResult):
    answer = []
    bonus = ['S', 'D', 'T']
    option = ['*', '#']
    idx = 0
    
    for i in range(len(dartResult)):
        if dartResult[i] in bonus:
            if dartResult[i] == 'S':
                answer.append(int(dartResult[idx:i]))
            elif  dartResult[i] == 'D':
                answer.append(int(dartResult[idx:i])**2)
            else:
                answer.append(int(dartResult[idx:i])**3)
            idx = i+1
            continue

        if dartResult[i] in option:
            if dartResult[i] == '*':
                answer_len = len(answer)
                if answer_len>1:
                    answer[len(answer)-2] = answer[len(answer)-2]*2
                answer[len(answer)-1] = answer[len(answer)-1]*2
            else:
                answer[len(answer)-1] = -answer[len(answer)-1]
            idx = i+1
            
    return sum(answer)