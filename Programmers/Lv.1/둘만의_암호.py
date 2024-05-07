# s 반복문
# if 조건문 == skip continue
# 새 문자열 += 문자열 + index % 26
def solution(s, skip, index):
    answer = ''
    def toNext (new_s):
        new_s = chr(ord('a') + (((ord(new_s) + 1) - ord('a'))) % 26)
        while new_s in skip:
            new_s = chr(ord('a') + (((ord(new_s) + 1) - ord('a'))) % 26)
        return new_s
        
    for new_s in s:
        for _ in range(index):
            new_s = toNext(new_s)
        answer += new_s
        
    return answer