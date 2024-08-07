from itertools import permutations

def solution(numbers):
    answer = 0
    comb_numbers = set()
    
    def is_prime(num):
        if 0<= num <= 1:
            return False
        if num <= 3:
            return True
        for n in range(2, num ** 1//2 + 1):
            if not num % n:
                return False
        return True
    
    for i in range(1, len(numbers)+1):
        comb_numbers.update([int(''.join(p)) for p in list(permutations(numbers, i))])

    for cn in comb_numbers:
        answer += is_prime(cn)

    return answer