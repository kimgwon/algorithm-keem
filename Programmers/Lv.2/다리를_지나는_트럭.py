from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    trucks_on_bridge = deque()
    trucks_on_bridge_weight = 0
    
    while truck_weights or trucks_on_bridge:
        answer += 1
        if trucks_on_bridge and trucks_on_bridge[0][1] <= answer-bridge_length:
            trucks_on_bridge_weight -= trucks_on_bridge.popleft()[0]
        
        if truck_weights and trucks_on_bridge_weight + truck_weights[0] <= weight:
            if len(trucks_on_bridge) < bridge_length:
                trucks_on_bridge.append((truck_weights.popleft(), answer))
                trucks_on_bridge_weight += trucks_on_bridge[-1][0]
    
    return answer