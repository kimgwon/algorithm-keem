from collections import deque
def solution(rows, columns, queries):
    answer = []
    graph = [[c+columns*r for c in range(1, columns+1)] for r in range(rows)]
    
    # (x1,y1)~(x1,y2),(x1+1,y2)~(x2,y2),(x2,y2-1)~(x2,y1),(x2-1,y1)~(x1,y1)
    def rotate(x1, y1, x2, y2):
        values = deque()
        idx = 0
        
        for i in range(y1, y2):
            values.append(graph[x1-1][i-1])
        for i in range(x1, x2):
            values.append(graph[i-1][y2-1])
        for i in range(y2, y1, -1):
            values.append(graph[x2-1][i-1])
        for i in range(x2, x1, -1):
            values.append(graph[i-1][y1-1])
            
        values.rotate(1)
        
        for i in range(y1, y2):
            graph[x1-1][i-1] = values[idx]
            idx+=1
        for i in range(x1, x2):
            graph[i-1][y2-1] = values[idx]
            idx+=1
        for i in range(y2, y1, -1):
            graph[x2-1][i-1] = values[idx]
            idx+=1
        for i in range(x2, x1, -1):
            graph[i-1][y1-1] = values[idx]
            idx+=1
            
        return min(values)
    
    for querie in queries:
        answer.append(rotate(*querie))
    
    return answer