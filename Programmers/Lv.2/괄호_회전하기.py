# def solution(s):
#     answer = 0
    
#     def is_right(s):
#         stack = []
#         for c in s:
#             if not stack:
#                 if c == ')' or c == '}' or c == ']':
#                     return False
#                 stack.append(c)
#                 continue
                
#             if c == ')' and stack[-1] == '(':
#                 stack.pop()
#             elif c == '}' and stack[-1] == '{':
#                 stack.pop()
#             elif c == ']' and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 stack.append(c)
                
#         return not stack
    
#     for i in range(len(s)):
#         if is_right(s):
#             answer += 1
#         s = s[1:] + s[0:1]
                
#     return answer
    
# return이 True면 1이다.
# rotate는 s[i:] + s[:i] 형식으로 구현할 수 있다.
def solution(s):
    answer = 0
    
    def is_right(s):
        stack = []
        for c in s:
            if not stack:
                if c == ')' or c == '}' or c == ']':
                    return False
                stack.append(c)
                continue
                
            if c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)
                
        return not stack
    
    for i in range(len(s)):
        answer += is_right(s[i:] + s[:i])
                
    return answer
    