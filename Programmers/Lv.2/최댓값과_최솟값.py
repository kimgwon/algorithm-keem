def solution(s):
    i = list(map(int, s.split(" ")))
    return str(min(i)) + " " + str(max(i))