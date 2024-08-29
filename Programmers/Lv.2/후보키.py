from itertools import combinations

def solution(relation):
    answer = 0
    row, column = len(relation[0]), len(relation)
    uniqueness = set()
    
    # 유일성 만족 체크
    def isUniqueness(keys):
        data = {tuple(item[key] for key in keys) for item in relation}
        return len(data) == column
    
    # 최소성 만족 체크
    def isMinimality(keys):
        for unique in uniqueness:
            # if sum([1 for key in keys if key in unique]) == len(unique):
            # 부분 집합 체크 함수
            if set(unique).issubset(keys):
                return False
        return True
    
    
    for n in range(1, len(relation)+1):
        for keys in combinations(range(row), n):
            if isMinimality(keys) and isUniqueness(keys):
                uniqueness.add(keys)
                answer += 1
            
    return answer

# issubset() : 집합 자료형에서 사용하는 메서드. 부분 집합 여부 확인