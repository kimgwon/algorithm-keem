import sys
input = sys.stdin.readline

while True:
    word = input().strip()
    if word == '0':
        break
    for i in range(len(word)//2 + 1):
        if word[i] != word[len(word) - i - 1]:
            print("no")
            break
    else:
        print("yes")