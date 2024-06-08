def solution(brown, yellow):
    # x * y = brown + yellow
    # x*2 + y*2 - 4 == brown -> x+y = (brown + 4) / 2
    # x = (brown + yellow) / y
    # x = (brown + 4) / 2 - y
    
    for i in range(1, brown + yellow) :
        if (brown + yellow) / i == (brown + 4) / 2 - i:
            return [(brown + yellow) / i, i]
    return [-1]