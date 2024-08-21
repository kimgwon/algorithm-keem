# from math import gcd
# def solution(arrayA, arrayB):
#     answer = []
    
#     arrayA.sort()
#     arrayB.sort()
    
#     gcd_A = gcd(arrayA[0], arrayA[1]) if len(arrayA)>1 else arrayA[0]
#     gcd_B = gcd(arrayB[0], arrayB[1]) if len(arrayB)>1 else arrayB[0]
    
#     # 최대공약수의 약수 구하는 함수
#     def find_gcd_divisors(gcd):
#         divisors = [gcd]
#         for i in range(2, gcd//2):
#             if gcd % i == 0:
#                 divisors += [i, gcd//i]
#         return sorted(divisors, reverse = True) if gcd > 1 else []
    
#     # array의 약수 구하는 함수
#     def find_divisors(arr, divisors, state):
#         result = []
#         for divisor in divisors:
#             if divisor <= 1:
#                 continue
#             for a in arr:
#                 if state == False and a % divisor == 0:
#                     break
#                 elif state == True and a % divisor != 0:
#                     break
#             else:
#                 result.append(divisor)
#         return result
    
#     gcd_A_divisors = find_gcd_divisors(gcd_A)
#     gcd_B_divisors = find_gcd_divisors(gcd_B)
    
#     A_divisors = find_divisors(arrayA, gcd_A_divisors, True)
#     B_divisors = find_divisors(arrayB, gcd_B_divisors, True)
    
#     answer = find_divisors(arrayA, B_divisors, False) + find_divisors(arrayB, A_divisors, False)
    
#     return sorted(answer)[-1] if answer else 0

# 최대공약수를 계속 누적하면 모든 원소의 최대공약수를 구할 수 있다...!!!
from math import gcd
def solution(arrayA, arrayB):
    answer = []
    gcd_a, gcd_b = arrayA[0], arrayB[0]
    
    for i in range(1, len(arrayA)):
        gcd_a = gcd(arrayA[i], gcd_a)
        gcd_b = gcd(arrayB[i], gcd_b)
    
    def is_not_div(arr, gcd):
        if gcd <= 1:
            return 0
        
        for a in arr:
            if a % gcd == 0:
                break
        else:
            return gcd
        
        return 0
    
    answer.extend([is_not_div(arrayA, gcd_b), is_not_div(arrayB, gcd_a)])
    
    return sorted(answer)[-1] if answer else 0