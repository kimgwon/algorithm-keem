# terms 반복문을 돌려서
# terms에 해당하는 약관을 먼저 구한다.
# privacies를 반복문을 돌려 날짜 비교를 한다.

# import math 
# def solution(today, terms, privacies):
#     answer = []
#     terms_dict = {}
    
#     for term in terms:
#         term_k, term_m = term.split(' ')
#         today_y, today_m, today_d = today.split('.')
#         m_distance = int(today_m) - int(term_m)
#         y, m, d = int(today_y), int(today_m) - int(term_m), int(today_d) + 1
        
#         if d == 29:
#             d = 1
#             m += 1
#         if m <= 0:
#             # 이럴경우 m은 0일때 y-1이 안된다..
#             y = str(y - math.ceil(abs(m) / 12))
#             m = 12 - abs(m) % 12
        
#         d = str(d) if d >= 10 else "0" + str(d)
#         m = str(m) if m >= 10 else "0" + str(m)
#         terms_dict[term_k] = str(y) + "." + m + "." + d
    
#     for idx, privacy in enumerate(privacies):
#         privacy_date, k = privacy.split(' ')
#         print(privacy_date, terms_dict[k])
#         if privacy_date < terms_dict[k]:
            
#             answer.append(idx+1)
    
#     return answer

def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    
    for term in terms:
        term_k, term_m = term.split(' ')
        today_y, today_m, today_d = today.split('.')
        m_distance = int(today_m) - int(term_m)
        y, m, d = int(today_y), int(today_m) - int(term_m), int(today_d) + 1
        
        if d == 29:
            d = 1
            m += 1
        if m <= 0:
            y = str(y - 1 - (abs(m) // 12))
            m = 12 - abs(m) % 12
        
        d = str(d) if d >= 10 else "0" + str(d)
        m = str(m) if m >= 10 else "0" + str(m)
        terms_dict[term_k] = str(y) + "." + m + "." + d
        
    for idx, privacy in enumerate(privacies):
        privacy_date, k = privacy.split(' ')
        if privacy_date < terms_dict[k]:
            answer.append(idx+1)
    
    return answer