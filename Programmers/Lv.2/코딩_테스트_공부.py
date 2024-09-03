def solution(alp, cop, problems):
    answer = 0
    
    # 필요한 최대 알고력과 코딩력을 구한다.
    # 반복문을 돌리며, 최대 알고력과 코딩력을 넘었으면 break
    # 1시간에 증가하는 알고력과 코딩력이 가장 큰 것을 한다.
    # -> 마지막에 1시간에 증가하는건 큰데 실제로 10시간, 다른건 1시간짜리가 있다면? NO
    
    # 백트래킹
    # 코딩력, 알고력 미달이면 return
    # 알,코 각 1씩 or problems 수 만큼 호출
    # 최대가 넘으면 최대에 넣기.
    
    max_alp, max_cop = 0, 0
    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])
        
    ability = []
    alp_times = [0 for _ in range((max_alp-alp)*2)]
    cop_times = [0 for _ in range((max_cop-cop)*2)]
    
    def backtrack(alp_times, cop_times, time):
        current_alp = alp_times[time]
        current_cop = cop_times[time]
        
        if current_alp >= max_alp and current_cop >= max_cop:
            answer = min(answer, time)
        
        for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
            if current_alp < alp_req or current_cop < alp_cop:
                continue
            if alp_times[time+cost] < alp_times[time]+alp_rwd and cop_times[time+cost] < cop_times[time]+alp_cop:
                temp = (alp_times[time+cost], cop_times[time+cost])
                alp_times[time+cost] = alp_times[time]+alp_rwd
                cop_times[time+cost] = cop_times[time]+alp_cop
                backtrack(alp_times, cop_times, time+cost)
                alp_times[time+cost] = temp[0]
                cop_times[time+cost] = temp[1]
            alp_times[time+1] = alp_times[time]+alp_rwd
            cop_times[time+1] = cop_times[time]+alp_cop
            backtrack(alp_times, cop_times, time+cost)
        
    
    return answer