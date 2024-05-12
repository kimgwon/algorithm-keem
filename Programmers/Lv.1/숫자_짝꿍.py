# X, Y를 각각 리스트로 만든다.
# X를 반복문으로 돌려서 Y안에 있는지 본다.
# 있다면 answer에 추가한다.
# answer이 빈 문자열이 아니라면 answer을 정렬한다.
# 빈 문자열 이라면 "-1"을 반환한다.

# 시간초과
; def solution(X, Y):
;     answer = ''
;     X = [i for i in str(X)]
;     Y = [i for i in str(Y)]
    
;     for x in X:
;         if x in Y:
;             answer += x
;             Y.remove(x)
            
;     answer = ''.join(sorted(answer, reverse = True))
;     if not answer:
;         answer = "-1"
            
;     return answer if answer[0] != "0" else "0"

def solution(X, Y):
    answer = ''
    
    for i in range(9,-1,-1):
        i = str(i)
        answer += i * min(X.count(i), Y.count(i))

    if not answer:
        answer = "-1"
    elif answer[0] == "0":
        answer = "0"
            
    return answer