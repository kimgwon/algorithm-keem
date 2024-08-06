def solution(numbers):
    answer = []
    
    def to_digit(number):
        digit = ""
        while number:
            digit += str(number%2)
            number //= 2
        return digit
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
            continue
            
        digit = list(map(int, to_digit(number)))
        for idx in range(len(digit)-1):
            if digit[idx] == 1 and digit[idx+1] == 0:
                digit[idx], digit[idx+1] = 0, 1
                break
        else:
            digit[-1] = 0
            digit.append(1)
        answer.append(sum([d * 2**i for i, d in enumerate(digit)]))
    
    return answer

# 10진수 -> 2진수 : bin()
# 2진수 -> 10진수 : int(2진수, 2)