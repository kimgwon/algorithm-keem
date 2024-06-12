def solution(n, words):
    use_words = []

    for i in range(len(words)):
        if words[i] in use_words:
            return [i % n + 1, i // n + 1]
        if use_words and words[i][0] != use_words[-1][-1]:
            return [i % n + 1, i // n + 1]
        use_words.append(words[i])

    return [0, 0]