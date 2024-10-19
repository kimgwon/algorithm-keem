# import sys
# input = sys.stdin.readline

# N = int(input().rstrip())
# times = [tuple(map(int, input().split(" "))) for _ in range(N)]
# times.sort(key = lambda x: (x[0], x[1]))

# rooms = []
# for start, end in times:
#     while rooms and rooms[-1][1] > end:
#         rooms.pop()

#     if not rooms or rooms[-1][1] <= start:
#         rooms.append((start, end))

# print(len(rooms))

import sys
input = sys.stdin.readline

N = int(input().rstrip())
times = [tuple(map(int, input().split())) for _ in range(N)]

# 끝나는 시간을 기준으로 정렬, 끝나는 시간이 같으면 시작 시간을 기준으로 정렬
times.sort(key=lambda x: (x[1], x[0]))
print(times)

max_meetings = 0
last_end_time = 0

for start, end in times:
    if start >= last_end_time:  # 회의가 끝난 이후에 시작할 경우 선택
        last_end_time = end
        max_meetings += 1

print(max_meetings)
