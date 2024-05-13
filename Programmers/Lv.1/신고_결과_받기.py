# id_list 만큼 dict에 key, list 만들어서 신고한 사람 이름 넣기
# 이미 리스트에 있으면 이름 안넣음
# 길이가 k 이상이면 해당 리스트에 있는 사람에게 메일
def solution(id_list, report, k):
    report_dict = {name : [] for name in id_list}
    mail_dict = {name : 0 for name in id_list}
    
    for r in report :
        from_id, to_id = r.split(' ')
        from_ids = report_dict[to_id]
        if from_id not in from_ids:
            report_dict[to_id].append(from_id)
    
    for to_id, from_ids in report_dict.items():
        if len(from_ids) >= k:
            for from_id in from_ids:
                mail_dict[from_id] += 1
    
    return (list(mail_dict.values()))

# set을 이용하여 중복을 제거할 수 있다.
# def solution(id_list, report, k):
#     report_dict = {name : [] for name in id_list}
#     mail_dict = {name : 0 for name in id_list}
    
#     for r in set(report) :
#         from_id, to_id = r.split(' ')
#         from_ids = report_dict[to_id]
#         report_dict[to_id].append(from_id)
    
#     for to_id, from_ids in report_dict.items():
#         if len(from_ids) >= k:
#             for from_id in from_ids:
#                 mail_dict[from_id] += 1
    
#     return (list(mail_dict.values()))