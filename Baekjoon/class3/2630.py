import sys
input = sys.stdin.readline

N = int(input().strip())
paper = [list(map(int, input().split(' '))) for _ in range(N)]
stack = [(0, 0, N)]
answer = [0, 0]

while stack:
    row, col, size = stack.pop()
    if all(paper[i][j] == paper[row][col] for j in range(col, col + size) for i in range(row, row + size)):
        answer[paper[row][col]] += 1
    else:
        half = size // 2
        stack.append((row, col, half))
        stack.append((row, col+half, half))
        stack.append((row+half, col, half))
        stack.append((row+half, col+half, half))

print(answer[0])
print(answer[1])