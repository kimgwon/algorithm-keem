import sys

input = sys.stdin.readline
T = int(input())

for t in range(T):
	x, y, n = map(int, input().split())
	if (n - (abs(x) + abs(y))) < 0 or (n - (abs(x) + abs(y))) % 2:
		print("NO")
	else :
		print("YES")