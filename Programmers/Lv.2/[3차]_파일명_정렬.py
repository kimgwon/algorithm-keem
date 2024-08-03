def solution(files):
    answer = []
    split_file = []
    
    for idx in range(len(files)):
        temp = []
        i = 0
        
        for f in files[idx]:
            if ord('0') <= ord(f) <= ord('9'):
                break
            i+=1
            
        temp.append(files[idx][:i].lower())
        
        j = i
        for f in files[idx][i:]:
            if ord(f.lower()) < ord('0')  or ord(f.lower()) > ord('9'):
                break
            j+=1
            
        temp.append(int(files[idx][i:j]))
        temp.append(idx)
        split_file.append(temp)
    
    split_file.sort(key = lambda x: (x[0], x[1], x[2]))
    
    return [files[sf[2]] for sf in split_file]