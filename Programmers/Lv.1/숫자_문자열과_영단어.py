def solution(s):
    number_list = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for idx in range(len(number_list)):
        if number_list[idx] in s:
            s = s.replace(number_list[idx], str(idx))
            
    return int(s)