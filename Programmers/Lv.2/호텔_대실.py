import heapq
from collections import deque

def solution(book_time):
    answer = 0
    book_time.sort(key = lambda x: x[0])
    books = deque([])
    room = []
    heapq.heapify(room)
    
    for start, end in book_time:
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))
        books.append([start_h * 60 + start_m, end_h * 60 + end_m])
    
    for t in range(23*60 + 59):
        if not books and not room:
            break
        
        # 퇴실
        while room:
            if room[0] == t:
                heapq.heappop(room)
            else:
                break
                
        # 입실
        while books:
            if books[0][0] == t:
                start, end = books.popleft()
                heapq.heappush(room, end+10)
                answer = max(answer, len(room))
            else:
                break
    
    return answer