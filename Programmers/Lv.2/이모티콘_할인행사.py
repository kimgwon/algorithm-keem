from itertools import product

def solution(users, emoticons):
    answer = []
    comb_discounts = product([10, 20, 30, 40], repeat = len(emoticons))
    
    for discount in comb_discounts:
        join, total_price = 0, 0
        for i in range(len(users)):
            rate, budget = users[i]
            price = 0
            for j in range(len(discount)):
                if discount[j] >= rate:
                    price += (emoticons[j] * (1-discount[j]/100))
            if price >= budget:
                join += 1
            else:
                total_price += price
        answer.append([join, total_price])
        
    return sorted(answer, key = lambda x: (-x[0], -x[1]))[0]