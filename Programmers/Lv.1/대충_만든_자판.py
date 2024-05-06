def solution(keymap, targets):
    answer = [0 for t in targets]
    index_dict = dict()
    
    # targets 반복문
    # targets[i] 반복문
    # (targets[i][j]가 keymap 리스트에 존재하는지 확인)
    # (확인된 인덱스는 딕셔너리에 저장하여 다시 검색하지 않도록 함)
    # keymap 반복문
    # keymap[a]에 targets[i][j]가 몇 번째 원소인지 확인 -> index
    # keymap[b]에 targets[i][j]가 몇 번째 원소인지 확인
    # 가장 빨리 나온 원소를 더함.
    
    for idx, target in enumerate(targets):
        for t in target:
            if t in index_dict:
                if index_dict[t] == -1:
                    answer[idx] = -1
                    break
                else:
                    answer[idx] += index_dict[t]
                    continue
                
            min_key = 101
            for k in keymap:
                if t in k:
                    min_key = min(min_key, k.find(t))
                    index_dict[t] = min_key+1
                    
            if min_key == 101:
                index_dict[t] = -1
                answer[idx] = -1
                break
                
            answer[idx] += index_dict[t]
    
    print(index_dict)
    return answer