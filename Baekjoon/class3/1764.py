import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
no_listen = set([input().rstrip() for _ in range(N)])
answer = []

for _ in range(M):
    person = input().rstrip()
    if person in no_listen:
        answer.append(person)

print(len(answer))
for person in sorted(answer):
    print(person)