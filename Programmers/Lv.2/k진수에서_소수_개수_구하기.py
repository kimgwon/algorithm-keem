def solution(n, k):
    answer = 0
    result = ''
    
    while n:
        result = str(n % k) + result
        n //= k
    
    result = [i for i in result.split('0') if i != '' and i != '1']
    
    for r in result:
        for i in range(2, int(int(r) ** 0.5) +1):
            if int(r)%i == 0:
                break
        else:
            answer += 1
    
    return answer