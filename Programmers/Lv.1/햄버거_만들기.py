# replace는 한번에 바꾼다.
# 반례 [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
# def solution(ingredient):
#     answer = 0
#     ingredient = ''.join(map(lambda x : str(x), ingredient))
    
#     while ingredient:
#         if '1231' in ingredient:
#             ingredient = ingredient.replace('1231', '')
#             answer+=1
#         else:
#             break
    
#     return answer


# stack에 들어간게 1이면 pop해서 1231이면 answer+1한다.
# def solution(ingredient):
#     answer = 0
#     hamburger = []
#     idx = 0
    
#     while idx < len(ingredient):
#         hamburger.append(str(ingredient[idx]))
#         idx+=1
        
#         if hamburger[-1] == '1' and len(hamburger) > 3:
#             if ''.join(hamburger[-4:]) == '1231' :
#                 for _ in range(4):
#                     hamburger.pop()
#                 answer+=1
    
#     return answer

# [:] 이렇게 범위 지정된거는 index오류가 나지 않는다.
def solution(ingredient):
    answer = 0
    hamburger = []
    
    for i in ingredient:
        hamburger.append(i)
        if hamburger[-4:] == [1,2,3,1]:
            for _ in range(4):
                hamburger.pop()
            answer+=1
    
    return answer