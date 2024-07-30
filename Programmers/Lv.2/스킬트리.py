def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        i = 0
        for st in skill_tree:
            if st not in skill:
                continue
            elif skill.index(st) <= i:
                i += 1
            else:
                break
        else:
            answer += 1
    return answer