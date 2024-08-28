def solution(m, musicinfos):
    answer = []
    
    def timeToInt(time):
        split_time = list(map(int, time.split(":")))
        return split_time[0]*60 + split_time[1]
    
    def sharpToLower(melodies):
        return melodies.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'a')
    
    m = sharpToLower(m)
    
    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, melodies = musicinfo.split(",")
        start = timeToInt(start)
        end = timeToInt(end)
        melodies = sharpToLower(melodies)
        
        share_time = (end-start) // (len(melodies))
        rest_time = (end-start) % (len(melodies))
        
        melodies = (melodies * share_time) + melodies[:rest_time]
        
        if m in melodies:
            answer.append([end-start, idx, title])
            
    answer.sort(key = (lambda x: (-x[0], x[1])))
    
    return answer[0][2] if answer else '(None)'