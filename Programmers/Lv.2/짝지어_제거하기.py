def solution(s):
    stack = [s[0]]
    
    for i in s[1:]:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
                
    return 0 if stack else 1