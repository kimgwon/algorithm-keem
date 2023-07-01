def toTwo(x):
    answer = ''
    while x!=0:
        answer+=str(x%2)
        x//=2
    return answer

def solution(s):
    result1, result2 = 0, 0
    
    while s!='1':
        new_s = ''.join([i for i in s if i=='1'])
        result1 += len(s)-len(new_s)
        s = toTwo(len(new_s))
        result2 +=1
        
    return [result2, result1]
