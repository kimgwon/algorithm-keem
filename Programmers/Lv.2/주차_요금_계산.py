import math

def solution(fees, records):
    answer = []
    cars_in = {}
    cars_out = {}
    
    for record in records:
        time, car, sign = record.split(" ")
        h, m = map(int, time.split(":"))
        time = h * 60 + m
        
        if sign == "IN":
            cars_in[car] = time
        elif sign == "OUT":
            cars_out[car] = cars_out.get(car, 0) + time - cars_in[car]
            del cars_in[car]
    
    for car, time in cars_in.items():
        cars_out[car] = cars_out.get(car, 0) + (23*60+59) - cars_in[car]
    
    for car, time in sorted(cars_out.items(), key = lambda x: x[0]):
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3])
            
    return answer