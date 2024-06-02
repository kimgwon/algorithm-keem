def solution(n):
    answer = bin(n)[2:].count('1')
    while answer != bin(n+1)[2:].count('1'):
        n += 1
    return n+1