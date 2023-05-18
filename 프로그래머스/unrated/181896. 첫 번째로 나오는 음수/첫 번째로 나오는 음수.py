def solution(num_list):
    answer = 0
    res = [[i, num] for i, num in enumerate(num_list) if num < 0]
    
    return res[0][0] if len(res) > 0 else -1