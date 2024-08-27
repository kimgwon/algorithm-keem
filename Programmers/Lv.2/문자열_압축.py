def solution(s):
    answer = len(s)
    
    for n in range(1, len(s)//2+1):
        result = []
        before = s[:n]
        cnt = 1
        for i in range(n, len(s), n):
            after = s[i:i+n]
            if before == after:
                cnt += 1
            else:
                result.append(str(cnt)+before if cnt>1 else before)
                before = after
                cnt = 1
        result.append(str(cnt)+before if cnt>1 else before)
        
        answer = min(answer, len(''.join(result)))
            
    return answer