def solution(prices):
    answer = [len(prices) - i - 1 for i in range(len(prices))]
    price_stack = []
    
    for i in range(len(prices)):
        while price_stack:
            if prices[price_stack[-1]] > prices[i]:
                j = price_stack.pop()
                answer[j] = i - j
            else:
                break
        price_stack.append(i)
                
    return answer