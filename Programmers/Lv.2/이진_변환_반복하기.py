def solution(s):
    cnt = 0
    sum_rm_0 = 0
    
    while s != '1' :
        cnt += 1
        rm_0 = s.count('0')
        sum_rm_0 += rm_0
        s = bin(len(s) - rm_0)[2:]
        print(bin(len(s) - rm_0))
        
    return [cnt, sum_rm_0]