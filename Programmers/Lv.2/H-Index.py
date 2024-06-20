# 내가 계속 시간 끌었던 풀이
def solution(citations):
    citations.sort()
    
    for i in range(len(citations)):
        if citations[i] > len(citations) - i:
            return len(citations)-i+1
        
    return -1

# 올바른 풀이
def solution(citations):
    citations.sort()
    
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations)-i
        
    return 0
