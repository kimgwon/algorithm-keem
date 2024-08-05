from collections import deque

def solution(m, n, board):
    answer = 0
    turn_board = []
    
    for i in range(n):
        turn = deque()
        for j in range(m):
            turn.append(board[m-j-1][i])
        turn_board.append(turn)
    
    while turn_board:
        removes = set()
        
        for i in range(len(turn_board)-1):
            for j in range(min(len(turn_board[i]), len(turn_board[i+1]))-1):
                if turn_board[i][j] == "-1":
                    continue
                if turn_board[i][j] == turn_board[i][j+1] == turn_board[i+1][j] == turn_board[i+1][j+1]:
                    removes.add((i,j))
                    removes.add((i,j+1))
                    removes.add((i+1,j))
                    removes.add((i+1,j+1))

        if not removes:
            break
            
        for i in range(n):
            for j in range(len(turn_board[i])):
                block = turn_board[i].popleft()
                if (i,j) not in removes:
                    turn_board[i].append(block)
                else:
                    answer += 1
                    
    return answer