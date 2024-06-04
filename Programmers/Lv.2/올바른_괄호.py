def solution(s):
    s_stack = []
    for i in s:
        if i == ')':
            if not s_stack:
                return False
            s_stack.pop()
        else:
            s_stack.append(i)
    else:
        if s_stack:
            return False
    return True