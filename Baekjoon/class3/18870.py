import sys
input = sys.stdin.readline

N = int(input().rstrip())
positions = [(value, idx) for idx, value in enumerate(map(int, input().split(" ")))]
positions.sort(key = lambda x: x[0])
answer = [0 for _ in range(N)]

result = 0
before = positions[0][0]
for value, idx in positions:
    if before == value:
        answer[idx] = result
    else:
        result += 1
        before = value
        answer[idx] = result

for result in answer:
    print(result, end = ' ')