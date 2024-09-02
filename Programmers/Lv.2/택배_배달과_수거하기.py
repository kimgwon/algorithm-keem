import heapq

def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver = []
    pick = []
    
    for i in range(n):
        if deliveries[i] > 0:
            heapq.heappush(deliver, (-i, deliveries[i]))
        if pickups[i] > 0:
            heapq.heappush(pick, (-i, pickups[i]))
    
    while deliver or pick:
        if deliver and not pick:
            answer += (-deliver[0][0]+1) * 2
        elif pick and not deliver:
            answer += (-pick[0][0]+1) * 2
        else:
            answer += max(-deliver[0][0]+1, -pick[0][0]+1)*2
        
        for i in range(cap):
            if deliver:
                d_idx, d_cnt = heapq.heappop(deliver)
                if d_cnt - 1 > 0:
                    heapq.heappush(deliver, (d_idx, d_cnt-1))
            if pick:
                p_idx, p_cnt = heapq.heappop(pick)
                if p_cnt -1 > 0 :
                    heapq.heappush(pick, (p_idx, p_cnt-1))
            
    return answer

# 누적합 이용
def solution(cap, n, deliveries, pickups):
    answer = 0
    
    for i in range(n-2, -1, -1):
        deliveries[i] += deliveries[i+1]
        pickups[i] += pickups[i+1]
        
    k = 0
    for i in range(n-1, -1, -1):
        while deliveries[i] > cap*k or pickups[i] > cap*k:
            answer += (i+1)*2
            k += 1
            
    return answer