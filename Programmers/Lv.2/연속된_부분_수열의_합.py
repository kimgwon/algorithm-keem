from collections import deque
def solution(sequence, k):
    answer = []
    sequence_queue = deque()
    sq_sum = 0
    start = 0
    
    for i in range(len(sequence)):
        sequence_queue.append(sequence[i])
        sq_sum += sequence_queue[-1]
        while sq_sum > k:
            sq_sum -= sequence_queue[0]
            sequence_queue.popleft()
            start += 1
        if sq_sum == k:
            if not answer or (answer[1] - answer[0] > i - start):
                answer = [start, i]
            
    return answer