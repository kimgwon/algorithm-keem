# 마지막 공격 시간 반복문
# 몬스터가 공격하는 시간이 아니라면 붕대감기 시작
# 몬스터가 공격하는 시간이라면 붕대 감은 시간만큼 체력 회복
# 이때 붕대 감은 시간이 시전 시간 이상이라면 시전 시간 * 초당 회복량 + 추가 회복량
# 이하라면 시전 시간 * 초당 회복량 + 추가 회복량
# 이때 최대 체력 이상이라면 최대 체력으로 초기화
# 초당 시간 초기화

def solution(bandage, health, attacks):
    band_time = 0
    attack_index = 0
    attack_time = [attack[0] for attack in attacks]
    current_health = health
    
    for game_time in range(1, attack_time[-1] + 1):
        if game_time not in attack_time:
            band_time += 1
        else:
            if band_time >= bandage[0]:
                current_health += (band_time//bandage[0]) * (bandage[0] * bandage[1] + bandage[2]) + (band_time%bandage[0]) * bandage[1]
            else:
                current_health += band_time * bandage[1]
                
            band_time = 0
            
            if current_health > health:
                current_health = health
            
            current_health -= attacks[attack_index][1]
            attack_index+=1
            
            if current_health <= 0:
                return -1
    
    return current_health