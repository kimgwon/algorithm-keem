# left~right가 몇 열의 몇 행인지
# n:3, left:2, right:5 일 때 
# arr[2] = (2//3) 행 (2%3) 열, arr[5] = (5//3) 행 (5%3) 열
# arr[2] = max(2//3,2%3) + 1
# arr[3] = max(3//3,3%3) + 1
# arr[5] = max(5//3, 5%3) + 1
def solution(n, left, right):
    return [max(idx//n, idx%n)+1 for idx in range(left, right+1)]