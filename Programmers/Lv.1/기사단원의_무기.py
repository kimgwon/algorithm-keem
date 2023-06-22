def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        temp = 0
        
        for j in range(1, int(i**(0.5))+1):
            if i%j==0:
                if i**(0.5) == j:
                    temp+=1
                else:
                    temp+=2
        
        if temp>limit:
            answer+=power
        else:
            answer+=temp
    
    return answer

# def solution(number, limit, power):
#     answer = 0
    
#     for i in range(1, number+1):
#         temp = 0
        
#         for j in range(1, int(i**(0.5))+1):
#             if i%j==0:
#                 temp+=1
                
#         if i == (i**(0.5))**2:
#             temp = (temp-1)*2+1
#         else:
#             temp*=2
        
#         if temp>limit:
#             answer+=power
#         else:
#             answer+=temp
    
#     return answer