from collections import Counter
def solution(nums):
    dict_nums = dict(Counter(nums))
    return len(dict_nums) if len(nums)//2>=len(dict_nums) else len(nums)//2