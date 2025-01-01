import sys
input = sys.stdin.readline

N = int(input().strip())

fib = [[0, 0] for _ in range(41)]
fib[0] = [1, 0]
fib[1] = [0, 1]

for i in range(2, len(fib)):
    fib[i][0] = fib[i-1][0] + fib[i-2][0]
    fib[i][1] = fib[i-1][1] + fib[i-2][1]

for _ in range(N):
    i = int(input().strip())
    print(fib[i][0], fib[i][1])