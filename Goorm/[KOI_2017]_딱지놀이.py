import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
for n in range(N):
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	
	A = defaultdict(int)
	B = defaultdict(int)
	for i in range(a[0]):
		A[a[i+1]] += 1
	for i in range(b[0]):
		B[b[i+1]] += 1
	
	for i in range(4,0,-1):
		if A[i] > B[i]:
			print('A')
			break
		elif A[i] < B[i]:
			print('B')
			break
	else:
		print("D")
print('')