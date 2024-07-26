# 시간 복잡도 O(n^2)으로 시간 초과..
# def solution(numbers):
#     answer = []
    
#     for i in range(len(numbers)):
#         for j in range(i, len(numbers)):
#             if numbers[i] < numbers[j]:
#                 answer.append(numbers[j])
#                 break
#         else:
#             answer.append(-1)
    
#     return answer

# O(n)으로 통과ㅋ
def solution(numbers):
    answer = [-1 for _ in numbers]
    number_stack = []
    
    for idx, number in enumerate(numbers):
        while number_stack:
            if number > number_stack[-1][1]:
                answer[number_stack[-1][0]] = number
                number_stack.pop()
            else:
                break
        number_stack.append((idx,number))
    
    return answer