def solution(progresses, speeds):
    answer = []
    deploy = []
    
    while progresses:
        for idx, speed in enumerate(speeds) :
            progresses[idx] += speed

        deploy = 0
        for progress in progresses:
            if progress >= 100:
                deploy += 1
            else:
                break
        
        if deploy > 0:
            answer.append(deploy)
            
        progresses = progresses[deploy:]
        speeds = speeds[deploy:]
            
    return answer

# 굳이 하루씩 계산할 필요 없다.
# 아래처럼 하면 O(n)이다.
# def solution(progresses, speeds):
#     print(progresses)
#     print(speeds)
#     answer = []
#     time = 0
#     count = 0
#     while progresses:
#         if (progresses[0] + time*speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer