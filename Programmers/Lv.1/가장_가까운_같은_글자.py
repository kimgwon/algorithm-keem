def solution(s):
    answer = []
    for idx in range(len(s)):
        result = s[:idx].rfind(s[idx])
        if result==-1:
            answer.append(-1)
        else:
            answer.append(idx-result)
    return answer