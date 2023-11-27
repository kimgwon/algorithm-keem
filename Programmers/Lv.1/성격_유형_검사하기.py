from collections import defaultdict

# survey[i]
#   1~3 -> 첫 번째 캐릭터
#   5~7 -> 두 번째 캐릭터

character_type = ["RT", "CF", "JM", "AN"]
value = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}

def solution(survey, choices):
    answer = ''
    
    survey_result = defaultdict(int)
    
    for s, c in zip(survey, choices):
        if 1<=c<=3:
            survey_result[s[0]] += value[c]
        elif 5<=c<=7:
            survey_result[s[1]] += value[c]
            
    for ct in character_type:
        a = survey_result[ct[0]]
        b = survey_result[ct[1]]
        
        if a>=b:
            answer+=ct[0]
        elif a<b:
            answer+=ct[1]
    
    return answer