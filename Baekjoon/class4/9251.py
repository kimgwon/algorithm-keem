import sys
from math import factorial
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
LCS = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            LCS[j][i] = LCS[j][i-1] + 1
        else:
            LCS[j][i] = max(LCS[j-1][i], LCS[j][i-1])

print(LCS[-1][-1])