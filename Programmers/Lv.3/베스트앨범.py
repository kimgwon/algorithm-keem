from collections import defaultdict

def solution(genres, plays):
    answer = []
    total_play = defaultdict(int)
    best = defaultdict(list)
    
    for idx in range(len(genres)):
        total_play[genres[idx]] += plays[idx]
        best[genres[idx]].append((plays[idx], idx))
        
    sorted_total_play = sorted(list(total_play.items()), key = lambda x: -x[1])
    
    for genre, total in sorted_total_play:
        best[genre].sort(key = lambda x: -x[0])
        size = min(2, len(best[genre]))
        for i in range(size):
            answer.append(best[genre][i][1])
    
    return answer