# def solution(s):
#     answer = 0
    
#     while len(s):
#         first = s[0]
#         count_x, count_not_x = 0, 0
        
#         for idx, x in enumerate(s):
                
#             if x == first:
#                 count_x += 1
#             else :
#                 count_not_x += 1
                
#             if count_x == count_not_x or idx+1 == len(s):
#                 answer += 1
#                 s = s[count_x + count_not_x:]
#                 break
            
#     return answer

def solution(s):
    answer = 0
    first = ""
    count_x, count_not_x = 0, 0
    
    for x in s:
        if count_x == 0 :
            first = x
            
        if first == x :
            count_x += 1
        else :
            count_not_x += 1
            
        if count_x == count_not_x:
            answer += 1
            count_x, count_not_x = 0, 0
            
    return answer if count_x == 0 else answer + 1