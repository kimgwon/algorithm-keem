def solution(n, info):
    MAX_SCORE = 10
    max_diff = 0
    answer = [0 for _ in range(MAX_SCORE+1)]
    
    def calculate_diff(lion_info):
        apeach, lion = 0, 0
        for i in range(MAX_SCORE):
            if info[i] > lion_info[i]:
                apeach += (MAX_SCORE - i)
            elif info[i] < lion_info[i]:
                lion += (MAX_SCORE - i)
        return lion - apeach
    
    def backtrack(n, idx, lion_info):
        nonlocal max_diff, answer
        
        if idx == MAX_SCORE+1 or n <= 0:
            lion_info[-1] += n
            current_diff = calculate_diff(lion_info)
            # 값 갱신 경우의 수 1: 현재 점수 차이가 더 크다.
            if current_diff > max_diff:
                max_diff = current_diff
                answer = lion_info[:]
            # 값 갱신 경우의 수 2: 점수 차이는 같지만, 적은 점수에 더 많이 쏘았다.
            elif current_diff == max_diff:
                for i in range(MAX_SCORE, -1, -1):
                    if lion_info[i] > answer[i]:
                        answer = lion_info[:]
                        break
                    elif lion_info[i] < answer[i]:
                        break
            lion_info[-1] -= n
            return
        
        # 경우의 수 1: 라이언이 쏜다.
        if info[idx]+1 <= n:
            lion_info[idx] = info[idx]+1
            backtrack(n - lion_info[idx], idx+1, lion_info)
            lion_info[idx] = 0
        # 경우의 수 2: 라이언이 안쏜다.
        backtrack(n, idx+1, lion_info)
        
    backtrack(n, 0, [0 for _ in range(MAX_SCORE+1)])
    
    return answer if max_diff else [-1]

# 첫번째 시도
# 화살을 쏠 때의 최적만 구하기 때문에 그 다음 최적은 구하지 못한다.
# import heapq
# def solution(n, info):
#     MAX_SCORE = 10
#     answer = [0 for _ in range(MAX_SCORE+1)]
#     arrows = []
    
#     def initOneArrowScore():
#         for i in range(MAX_SCORE+1):
#             one_arrow_score = (MAX_SCORE - i) / (info[i]+1)
#             if info[i] > 0:
#                 one_arrow_score *= 2
#             heapq.heappush(arrows, (-one_arrow_score, (MAX_SCORE - i), info[i] + 1))
            
#     def getScore(n):
#         while arrows:
#             if n <= 0:
#                 break
                
#             one_arrow_score, score, arrow_cnt = heapq.heappop(arrows)
            
#             if arrow_cnt > n:
#                 continue
#             n -= arrow_cnt
#             answer[MAX_SCORE - score] = arrow_cnt
        
#         if n:
#             answer[-1] = n
            
#     def isHighLionScore():
#         apeach_score, lion_score = 0, 0
#         for i in range(MAX_SCORE+1):
#             if info[i] > answer[i]:
#                 apeach_score += MAX_SCORE - i
#             elif info[i] < answer[i]:
#                 lion_score += MAX_SCORE - i
#         return True if lion_score > apeach_score else False
            
#     initOneArrowScore()
#     getScore(n)
    
#     return answer if isHighLionScore() else [-1]