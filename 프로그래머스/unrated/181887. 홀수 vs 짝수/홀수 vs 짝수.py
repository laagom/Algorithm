def solution(num_list):
    sum_odd = 0
    sum_oven = 0
    
    for i, num in enumerate(num_list):      
        if i%2 == 0:
            sum_oven += num
        else:
            sum_odd += num           
    return sum_oven if sum_oven >= sum_odd else sum_odd