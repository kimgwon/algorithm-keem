def solution(n, lost, reserve):
    for student in range(1, n+1):
        if student in reserve:
            if student in lost:
                lost.remove(student)
                reserve.remove(student)
            elif student-1 in lost and student-1 not in reserve:
                lost.remove(student-1)
                reserve.remove(student)
            elif student+1 in lost and student+1 not in reserve:
                lost.remove(student+1)
                reserve.remove(student)
    
    return n - len(lost)