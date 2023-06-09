def solution(a, b):
    calendar = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    answer = (day.index("FRI") + sum([calendar[idx] for idx in range(a-1)]) + b -1) % len(day)
    
    return day[answer]