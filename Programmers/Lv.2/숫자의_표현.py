
# def solution(n):
#     answer = 1
#     for i in range(1, round(n/2)+1):
#         temp = 0
#         for j in range(i, n):
#             temp+=j
#             if temp>=n:
#                 break
#         if temp==n:
#             answer+=1
#     return answer