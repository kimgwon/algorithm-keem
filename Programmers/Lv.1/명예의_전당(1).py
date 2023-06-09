from heapq import heapify, heappush, heappop
def solution(k, score):
    answer = []
    heap = []
    
    for i in range(len(score)):
        heappush(heap, score[i])
        if k<i+1:
            heappop(heap)
        answer.append(heap[0])
        
    return answer