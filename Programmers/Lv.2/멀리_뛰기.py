# 바로 전 데이터에 1을 더하기 또는 한 칸 전까지의 데이터가 1이면 2를 더하기
# 1: 1
# 2: 1,1 / 2
# 3: 1,1,1 / 1,2 / 2,1
# 4: 1,1,1,1 / 1,1,2 / 1,2,1 / 2,1,1 / 2,2
# 5: 1,1,1,1,1 / 1,1,1,2 / 1,1,2,1 / 1,2,1,1 / 1,2,2 / 2,1,1,1 / 2,1,2 / 2,2

def solution(n):
    answer = 0
    a, b = 1, 2
    for i in range(n-1):
        a, b =  b, a+b
        
    return a % 1234567