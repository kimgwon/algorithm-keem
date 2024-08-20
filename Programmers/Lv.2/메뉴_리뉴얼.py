from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    for idx, order in enumerate(orders):
        order = ''.join(sorted([o for o in order]))
        orders[idx] = order
    
    for c in course:
        order_dict = defaultdict(int)
        for order in orders:
            if len(order) < c:
                continue
            for comb_order in list(combinations(order, c)):
                order_dict[''.join(comb_order)] += 1
        order_dict = sorted(order_dict.items(), key = lambda x: -x[1])
        if order_dict:
            max_order = order_dict[0][1]
            if max_order <= 1:
                break
            for od in order_dict:
                if od[1] == max_order:
                    answer.append(od[0])
    
    return sorted(answer)

# 개선사항
# 문자열.sort()는 안되지만, sorted(문자열)은 된다.
# dict 대신 Counter로 횟수를 센다.
# 반복문을 한 줄로 줄이기...
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        comb_order = []
        for order in orders:
            comb_order.extend(combinations(sorted(order), c))
        order_cnt = sorted(Counter(comb_order).items(), key = lambda x: -x[1])
        answer.extend([''.join(o) for o, c in order_cnt if c>1 and c == order_cnt[0][1]])
    
    return sorted(answer)