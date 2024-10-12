# 풀이 1 : 백트래킹
def solution(begin, target, words):
    MAX_INT = int(1e9)
    answer = MAX_INT
    visited = [False for _ in range(len(words))]
    
    def backtrack(word, visited, cnt):
        nonlocal answer
        
        if word == target:
            answer = min(answer, cnt)
        
        for j in range(len(words)):
            if visited[j]:
                continue
                
            diff = 0
            for x, y in zip(word, words[j]):
                if x != y:
                    diff += 1
                if diff >= 2:
                    break
                    
            if diff == 1:
                visited[j] = True
                backtrack(words[j], visited[:], cnt+1)
                visited[j] = False
                
    backtrack(begin, visited[:], 0)
    
    return answer if answer < MAX_INT else 0

# BFS 이용
from collections import deque

def solution(begin, target, words):
    MAX_INT = int(1e9)
    answer = MAX_INT
    
    def isDiffrentOneLetter(word1, word2):
        diff = 0
        for x, y in zip(word1, word2):
            if x != y:
                diff += 1
            if diff >= 2:
                break
        return True if diff==1 else False
    
    def bfs(word):
        queue = deque()
        queue.append((word, 0))
        visited = [False for _ in range(len(words))]
        
        while queue:
            word, cnt = queue.popleft()
            if word == target:
                return cnt
            for i in range(len(words)):
                if visited[i]:
                    continue
                if isDiffrentOneLetter(word, words[i]):
                    queue.append((words[i], cnt+1))
                    visited[i] = True
        return 0
    
    return bfs(begin)