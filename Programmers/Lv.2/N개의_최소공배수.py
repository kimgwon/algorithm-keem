def solution(arr):
    idx = 2
    answer = arr[-1]
    
    while True:
        for a in arr:
            if answer % a != 0:
                answer = arr[-1] * idx
                idx += 1
                break
        else:
            break
            
    return answer