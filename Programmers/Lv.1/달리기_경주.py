# 시간 초과
# def solution(players, callings):
#     for calling in callings:
#         idx = players.index(calling)
#         players[idx], players[idx-1] = players[idx-1], players[idx]
        
#     return players

def solution(players, callings):
    players_rank = {players[i] : i for i in range(len(players))}
    
    for calling in callings:
        rank = players_rank[calling]
        players_rank[calling] = rank - 1
        players_rank[players[rank-1]] = rank
        players[rank], players[rank-1] = players[rank-1], players[rank]
        
    return players