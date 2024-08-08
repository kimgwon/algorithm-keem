def solution(arr):
    answer = [0, 0]
    
    def to_zip(row, col, n):
        cnt = [0, 0]
        
        for r in range(row, row+n):
            for c in range(col, col+n):
                cnt[arr[r][c]] += 1
                
        if n**2 in cnt:
            answer[arr[r][c]] += 1
            return
        
        n//=2
        
        if n<=1:
            answer[0] += cnt[0]
            answer[1] += cnt[1]
        else:
            to_zip(row, col, n)
            to_zip(row+n, col, n)
            to_zip(row, col+n, n)
            to_zip(row+n, col+n, n)

    to_zip(0, 0, len(arr))
    return answer