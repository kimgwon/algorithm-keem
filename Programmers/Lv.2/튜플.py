def solution(s):
    answer = []
    arr = list(map(lambda x: list(map(int, x.split(","))), s[2:-2].split("},{")))
    arr.sort(key = lambda x: len(x))
    
    for i in arr:
        for j in i:
            if j not in answer:
                answer.append(j)
                break
        
    return answer