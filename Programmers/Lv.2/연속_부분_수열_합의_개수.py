# def solution(elements):
#     answer = set()
#     for i in range(1, len(elements)):
#         for _ in range(len(elements)):
#             answer.add(sum(elements[0:i]))
#             elements = elements[1:] + elements[0:1]
#     return len(answer) + 1

# 자르지 않고 기존에 있던 값에 더하면서 구할 수 있다.
def solution(elements):
    answer = set()
    for i in range(len(elements)):
        temp = 0
        for j in range(0, len(elements)-1):
            temp += elements[(i+j) % len(elements)]
            answer.add(temp)
    return len(answer) + 1