def solution(record):
    answer = []
    status_message = {"Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."}
    uids = {}
    
    for r in record:
        if r[0] != "L":
            status, uid, nickname = r.split(" ")
            uids[uid] = nickname
        
    for r in record:
        if r[0] != "C":
            r = r.split(" ")
            answer.append(uids[r[1]]+status_message[r[0]])
    
    return answer