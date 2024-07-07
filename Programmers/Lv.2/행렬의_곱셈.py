def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2[0])):
            temp.append(sum([arr1[i][k] * arr2[k][j] for k in range(len(arr2))]))
        answer.append(temp)
    return answer

# 언패킹 연산자 이용
def solution2(arr1, arr2):
    answer = []
    for arr1_row in arr1:
        temp = []
        for arr2_row in zip(*arr2):
            temp.append(sum([i*j for i, j in zip(arr1_row, arr2_row)]))
        answer.append(temp)
    return answer