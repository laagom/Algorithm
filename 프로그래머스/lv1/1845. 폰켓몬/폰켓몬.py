from collections import Counter

def solution(nums):
    count_dict = Counter(nums)

    answer = len(nums)/2 if len(count_dict) > len(nums)/2 else len(count_dict) 
    
    return answer