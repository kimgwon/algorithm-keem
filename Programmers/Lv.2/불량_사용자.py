def solution(user_id, banned_id):
    answer = set()
    
    def backtrack(idx, is_banned_user_id, is_banned_id):
        if False not in is_banned_id:
            answer.add(tuple(is_banned_user_id[:]))
            return
        
        if idx == len(user_id):
            return
        
        for i in range(len(banned_id)):
            if is_banned_id[i]:
                continue
            if len(user_id[idx]) != len(banned_id[i]):
                continue
            for j in range(len(banned_id[i])):
                if banned_id[i][j] == '*':
                    continue
                if banned_id[i][j] != user_id[idx][j]:
                    break
            else:
                is_banned_user_id[idx] = True
                is_banned_id[i] = True
                backtrack(idx+1, is_banned_user_id, is_banned_id)
                is_banned_user_id[idx] = False
                is_banned_id[i] = False
        backtrack(idx+1, is_banned_user_id, is_banned_id)
                    
    backtrack(0, [False]*len(user_id), [False]*len(banned_id))
    
    return len(answer)

# 순열 이용한 풀이
# from itertools import permutations

# def solution(user_id, banned_id):
#     def match(banned, user):
#         if len(banned) != len(user):
#             return False
#         for b, u in zip(banned, user):
#             if b != '*' and b != u:
#                 return False
#         return True

#     possible_matches = []
#     for banned in banned_id:
#         possible_matches.append([user for user in user_id if match(banned, user)])

#     valid_combinations = set()
#     for comb in permutations(user_id, len(banned_id)):
#         if all(comb[i] in possible_matches[i] for i in range(len(banned_id))):
#             valid_combinations.add(tuple(sorted(comb)))

#     return len(valid_combinations)
