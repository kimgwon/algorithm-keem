import sys
input = sys.stdin.readline

operator = { '+', '-', '*', '/' }
stack = []
answer = ''

for i in input().strip():
    if i == '(' :
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and (stack[-1] in operator):
            answer += stack.pop()
        stack.append(i)
    else:
        answer += i

while stack:
    answer += stack.pop()

print(answer)