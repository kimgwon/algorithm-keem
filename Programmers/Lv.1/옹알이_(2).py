def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]

    for one_babbling in babbling:
        compare_word = ""
        last_word = ""

        for word in one_babbling :
            compare_word += word
            if compare_word == last_word :
                break
            if compare_word in possible :
                last_word = compare_word
                compare_word = ""

        if compare_word == "" :
            answer +=1

    return answer