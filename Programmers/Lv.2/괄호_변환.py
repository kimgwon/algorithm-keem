def solution(p):
    answer = ''
    if not p:
        return ''
    
    # 균형잡힌 괄호 문자열로 분리하는 함수
    def separator(s):
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                return [s[:i+1], s[i+1:]]
        return ['', '']
    
    # 올바른 문자열인지 확인하는 함수
    def isRight(s):
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            elif s[i] == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[i])
                
        return True if not stack else False

    # 올바른 문자열로 변환하는 함수
    def toRight(s):
        u, v = separator(s)
        
        if not u:
            return ''
    
        if isRight(u):
            return u + toRight(v)
        else:
            return '(' + toRight(v) + ')' + ''.join(['(' if i==')' else ')' for i in u])[1:-1]

    return toRight(p)