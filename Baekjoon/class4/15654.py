import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(" "))
nums = sorted(list(map(int, input().split(" "))))

queue = deque()
queue.append([])
while queue:
    progression = queue.popleft()
    if len(progression) == M:
        print(*progression)
        continue
    
    for i in range(N):
        if nums[i] not in progression:
            queue.append(progression + [nums[i]])

# 백트래킹 풀이
# # 입력 받기
# N, M = map(int, input().split())
# numbers = list(map(int, input().split()))

# # 수를 사전 순으로 정렬
# numbers.sort()

# # 방문 여부를 체크할 리스트
# visited = [False] * N
# result = []

# def backtrack(depth):
#     # M개의 숫자를 선택했을 때 출력
#     if depth == M:
#         print(" ".join(map(str, result)))
#         return

#     # 각 숫자를 순서대로 선택
#     for i in range(N):
#         if not visited[i]:  # 숫자가 선택되지 않았을 경우
#             visited[i] = True
#             result.append(numbers[i])
#             backtrack(depth + 1)
#             # 백트래킹: 선택 해제 및 결과 초기화
#             result.pop()
#             visited[i] = False

# # 백트래킹 함수 호출
# backtrack(0)

# 순열 풀이
# from itertools import permutations

# # 입력 받기
# N, M = map(int, input().split())
# numbers = list(map(int, input().split()))

# # 주어진 수를 사전 순으로 정렬
# numbers.sort()

# # 순열을 이용해 N개의 수에서 M개를 선택한 모든 경우의 수 생성
# perms = permutations(numbers, M)

# # 결과 출력
# for perm in perms:
#     print(" ".join(map(str, perm)))
