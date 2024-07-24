from itertools import product

def solution(word):
    alpha = [a for a in "AEIOU"]
    words = []
    
    for i in range(1, 6):
        for a in product(alpha, repeat=i):
            words.append(''.join(a))
    
    return sorted(words).index(word) + 1