def digit(x, n):
    result = ''
    while x:
        rest = x % n
        if rest >= 10:
            rest = chr(ord('A') + rest % 10)
        result += str(rest)
        x //= n
    return result if result else '0'

def solution(n, t, m, p):
    answer = ''
    digit_result = ''
    num = 0
    
    for i in range(m * (t-1) + p):
        if not digit_result:
            digit_result = digit(num, n)
            num += 1
        if i % m == p-1:
            answer += digit_result[-1]
        digit_result = digit_result[:-1]
        
    return answer