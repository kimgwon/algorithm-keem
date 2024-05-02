# 두 사람이 선물을 주고 받았는지?
# 그 사람의 선물 지수가 몇인지? -> {}
# 이번달 선물을 몇 개 받는지? -> {}

# gifts 반복문을 돌린다.
# gift[0] 선물지수 딕셔너리 +1을 한다.
# friends 이중 반복문을 돌린다.
# gift 내 "friend1 friend2"와 "friend2 friend1"의 개수를 비교한다.
# 개수가 0이 아니고 다르다면
#   많은 사람의 선물 딕셔너리 +1을 한다.
# 개수가 0이거나 같다면
#   선물 지수가 높은 사람의 선물 딕셔너리 +1을 한다.

def solution(friends, gifts):
    answer = 0
    gift_dict = {friend : 0 for friend in friends}
    next_month_gift_dict = {me : 0 for me in friends}
    
    for gift in gifts:
        give, take = gift.split()
        gift_dict[give] += 1
        gift_dict[take] -= 1
        
    for idx in range(len(friends)-1):
        f1 = friends[idx]
        for f2 in friends[idx+1:]:
            f1_give = gifts.count(f1 + " " + f2)
            f2_give = gifts.count(f2 + " " + f1)
            
            if f1_give > f2_give:
                next_month_gift_dict[f1] += 1
            elif f1_give < f2_give:
                next_month_gift_dict[f2] += 1
            else:
                if gift_dict[f1] > gift_dict[f2]:
                    next_month_gift_dict[f1] += 1
                elif gift_dict[f1] < gift_dict[f2]:
                    next_month_gift_dict[f2] += 1
    
    return max(next_month_gift_dict.values())