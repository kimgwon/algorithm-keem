import math

def solution(w,h):
    return w*h - (w + h - math.gcd(w,h))

# w,h가 클 때 부동소수점 오차로 인해 틀린 결과가 나올 수 있다.
# import math

# def solution(w,h):
#     answer = 0
#     w, h = min(w,h), max(w,h)
#     y1 = 0
    
#     for x in range(w):
#         y2 = h/w * (x+1)
#         answer += (math.ceil(y2) - math.floor(y1))
#         y1 = y2
        
#     return w*h - answer