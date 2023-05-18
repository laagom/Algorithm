def solution(num_list, n):
    flag = False
    for num in num_list:
        if num == n:
            flag = True
    return 1 if flag else 0