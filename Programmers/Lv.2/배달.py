import sys
sys.setrecursionlimit(10**7)

def solution(N, road, K):
    delievers = [500000] * N
    delievers[0] = 0
    road = [[min(start,end), max(start,end), time] for start, end, time in road]

    def dfs(start, end, time):
        if delievers[end-1] > delievers[start-1] + time:
            delievers[end-1] = delievers[start-1] + time
            for n_start, n_end, n_time in road:
                if end == n_start:
                    dfs(n_start, n_end, n_time)
                elif end == n_end:
                    dfs(n_end, n_start, n_time)
    
    for start, end, time in road:
        if start == 1:
            dfs(start, end, time)
    
    return len([d for d in delievers if d<=K])