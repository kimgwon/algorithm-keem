# from heapq import heappush, heappop
# def solution(k, m, score):
#     answer = 0
#     heap = []
#     for s in score:
#         heappush(heap, -s)
    
#     for i in range(len(score)//m):
#         temp = []
#         for j in range(m):
#             if j>=len(score):
#                 break
#             temp.append(-heappop(heap))
#         answer+=min(temp)*m
    
#     return answer

def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

# list step
# A = [1,2,3,4,5,6,7,8,9]일 때 A[::3] >>> [1,4,7]
# A = [1,2,3,4,5,6,7,8,9]일 때 A[1:7:3] >>>  [2,5]