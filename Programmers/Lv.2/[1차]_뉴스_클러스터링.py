import re
import math
def split_word(str1):
    word_dict = {}
    
    for idx in range(len(str1)-1):
        word = str1[idx:idx+2].lower()
        if word == re.sub("[^a-z]", "", word):
            word_dict[word] = word_dict.get(word, 0) + 1
            
    return word_dict


def solution(str1, str2):
    answer = 0
    
    str1_dict = split_word(str1)
    str2_dict = split_word(str2)
    str1_set = set(str1_dict.keys())
    str2_set = set(str2_dict.keys())
    
    str_union = sum([max(str1_dict.get(key,0), str2_dict.get(key,0)) for key in str1_set|str2_set])
    str_intersection = sum([min(str1_dict.get(key,0), str2_dict.get(key,0)) for key in str1_set&str2_set])
    
    if str_intersection==0 and str_union==0:
        answer = 1
    elif str_union == 0:
        answer = 0
    else:
        answer = str_intersection / str_union
    
    return math.floor(answer*65536)