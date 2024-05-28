def solution(phone_number):
    phone_len = len(phone_number)
    return ''.join(["*" for i in range(0, phone_len-4)]+[phone_number[i] for i in range(phone_len-4,phone_len)])