# def solution(N, stages):
#     answer = []
#     user = len(stages)
#     fail = dict()
#     for stage in range(1, N+1):
#         if user<=0:
#             fail[stage] = 0
#         else:
#             fail[stage] = stages.count(stage)/user
#             user-=stages.count(stage)

#     answer = list(map(lambda x: x[0], sorted(fail.items(), key = lambda x:x[1], reverse=True)))
    
    
#     return answer

from collections import Counter

def solution(N, stages):
    answer = []
    user = len(stages)
    fail = dict(Counter(stages))
    
    if N+1 in fail:
        del fail[N+1]
    
    for stage in range(1, N+1):
        if stage not in fail:
            fail[stage] = 0
        
        if user<=0:
            fail[stage] = 0
        else:
            fail[stage] = fail[stage]/user
            user-=stages.count(stage)

    answer = list(map(lambda x: x[0], sorted(sorted(fail.items()), key = lambda x:x[1], reverse=True)))
    
    
    return answer