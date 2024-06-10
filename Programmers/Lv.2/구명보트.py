# 가장 가벼운 사람을 담는다. (left)
# 담을 수 있는 가장 무거운 사람을 담는다. (right)
# right 이후의 사람들은 모두 새 보트에 담는다.
# 그 다음 무거운 사람을 새 보트에 담는다.

def solution(people, limit):
    people.sort()
    boat = 0
    left, right = 0, len(people)-1
    
    while left <= right:
        p1 = people[left]
        boat += 1
        
        for i in range(right, left, -1):
            if p1 + people[i] <= limit:
                boat += (right - i)
                right = i - 1
                break
        else:
            boat += (right - left)
            right = left
        
        left += 1
    
    return boat