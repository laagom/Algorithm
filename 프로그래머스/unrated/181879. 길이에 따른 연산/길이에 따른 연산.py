def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        answer = eval('+'.join(list(map(str,num_list))))
    else:
        answer = eval('*'.join(list(map(str,num_list))))
    return answer