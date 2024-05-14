import re
def solution(new_id):
    new_id = new_id.lower()
    
    new_id = re.sub('[^a-z0-9\-\_\.]', '', new_id)
    
    is_dot = False
    temp = ''
    for i in new_id:
        if i != '.':
            temp += i
            is_dot = False
        else:
            if not is_dot:
                temp += i
                is_dot = True
    new_id = temp
    
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
        
    if not new_id:
        new_id = 'a'
        
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3-len(new_id))
    
    return new_id

# 정규 표현식 사용
# import re
# def solution(new_id):
#     new_id = new_id.lower()
    
#     new_id = re.sub('[^a-z0-9\-\_\.]', '', new_id)
#     new_id = re.sub('\.{2,}', '.', new_id)
#     new_id = re.sub('^[.]|[.]$', '', new_id)
#     new_id = 'a' if not new_id else new_id[:15]
#     new_id = re.sub('[.]$', '', new_id)
#     new_id = new_id if len(new_id) > 2 else new_id + new_id[-1] * (3-len(new_id))
    
#     return new_id