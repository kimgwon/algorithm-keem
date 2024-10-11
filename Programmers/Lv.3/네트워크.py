def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def bfs(i):
        stack = [j for j in range(len(computers[i])) if computers[i][j] and not visited[j]]
        network = set()
        while stack:
            j = stack.pop()
            if visited[j]:
                continue
            visited[j] = True
            network.add(j)
            stack += [k for k in range(len(computers[j])) if computers[j][k] and not visited[k]]
            
        return 1 if network else 0
            
    for i in range(len(computers)):
        if not visited[i]:
            answer += bfs(i)
        
    return answer