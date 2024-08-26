import heapq

def solution(picks, minerals):
    answer = 0
    minerals = minerals[:sum(picks)*5]
    mountain = []
    stress = {"diamond" : [1,5,25], "iron" : [1,1,5], "stone" : [1,1,1]}
    
    for i in range(0, len(minerals), 5):
        group = minerals[i:i+5]
        group_stress = sum(stress[m][2] for m in group)
        heapq.heappush(mountain, (-group_stress, group))
        
    while mountain:
        mineral = heapq.heappop(mountain)[1]
        
        if picks[0]:
            pick = 0
        elif picks[1]:
            pick = 1
        else:
            pick = 2
        picks[pick] -= 1
        
        for m in mineral:
            answer += stress[m][pick]
    
    return answer