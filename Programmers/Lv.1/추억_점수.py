def solution(name, yearning, photo):
    answer = []
    memory = dict(zip(name,yearning))
    for one_photo_list in photo:
        result = 0
        for one_photo in one_photo_list:
            if one_photo in memory:
                result+=memory[one_photo]
        answer.append(result)
    return answer