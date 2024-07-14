from itertools import permutations

def solution(k, dungeons):
    answer = 0
    p_dungeons = list(permutations(dungeons))
    
    for dungeon in p_dungeons:
        temp_k = k
        cnt = 0
        for need_stress, use_stress in dungeon:
            if temp_k < need_stress:
                break
            temp_k -= use_stress
            cnt += 1
        answer = max(answer, cnt)
        if answer==len(dungeons):
            break
    
    return answer

# dfs 풀이
# def dfs(k, dungeons, visited, count):
#     global max_dungeons  # 전역 변수를 통해 최대 던전 수 관리
#     max_dungeons = max(max_dungeons, count)  # 탐험한 던전 수 갱신
    
#     for i in range(len(dungeons)):
#         min_fatigue, cost_fatigue = dungeons[i]
        
#         if not visited[i] and k >= min_fatigue:  # 아직 탐험하지 않았고 탐험 가능하면
#             visited[i] = True  # 던전 방문 표시
#             dfs(k - cost_fatigue, dungeons, visited, count + 1)  # 탐험 후 다음 던전 탐색
#             visited[i] = False  # 던전 방문 해제 (다른 경로에서 다시 탐험할 수 있도록)

# def solution(k, dungeons):
#     global max_dungeons
#     max_dungeons = 0  # 최대 던전 수 초기화
    
#     visited = [False] * len(dungeons)  # 던전 방문 여부 체크용 리스트
#     dfs(k, dungeons, visited, 0)  # 초기 피로도와 함께 DFS 탐색 시작
    
#     return max_dungeons
