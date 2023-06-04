# def solution(t, p):
#     answer=0
#     t_list = []
    
#     for i in range(0, len(t)-len(p)+1):
#         t_list.append(t[i:i+len(p)])
        
#     for i in range(len(t_list)):
#         if int(p)>=int(t_list[i]):
#             answer+=1
            
#     return answer

def solution(t, p):
    answer=0
            
    for i in range(len(t)-len(p)+1):
        if int(p)>=int(t[i:i+len(p)]):
            answer+=1
    
    return answer