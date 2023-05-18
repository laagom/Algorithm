def solution(num_list):
    answer = 1
    length = len(num_list)
    if length >= 11:
        answer = sum(num_list)
    else:
        bs_num = 1
        for num in num_list:
            bs_num *= num
        answer = bs_num
    return answer