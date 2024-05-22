# board[x][0] : 첫번째 인형
# moves 반복문
# move는 x
# board[x][0] ~ board[x][y] 까지 순회하며 값이 나오면 선택
# basket[-1]과 선택된 인형이 같으면 pop후 answer + 2
# def solution(board, moves):
#     answer = 0
#     x = len(board[0])
#     y = len(board)
#     basket = []
    
#     for move in moves:
#         hold = 0
#         for i in range(y):
#             hold = board[i][move-1]
#             if hold != 0:
#                 board[i][move-1] = 0
#                 break
        
#         if hold == 0:
#             continue
            
#         if not basket:
#             basket.append(hold)
#         elif basket[-1] == hold:
#             basket.pop()
#             answer += 2
#         else:
#             basket.append(hold)
            
#     return answer

# 좀 더 간략하게
def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                basket.append(board[i][move-1])
                board[i][move-1] = 0
                break
        
        if len(basket) >= 2:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer+=2
            
    return answer