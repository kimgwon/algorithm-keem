from collections import deque
from collections import Counter

def solution(topping):
    answer = 0
    topping = deque(topping)
    chul = set()
    chul_bro = dict(Counter(topping))
    
    for i in range(len(topping)):
        move = topping.popleft()
        chul.add(move)
        
        if chul_bro[move] <= 1:
            del chul_bro[move]
        else:
            chul_bro[move] -= 1
            
        if len(chul) == len(chul_bro):
            answer += 1
            
    return answer

# list() -> set() : O(N)
# list slicing : O(N)