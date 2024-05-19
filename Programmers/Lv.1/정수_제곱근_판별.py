def solution(n):
    return (n**0.5+1)**2 if int(n**0.5) == n**0.5 else -1

# 반내림 함수가 생각 안났다.
# math.floor