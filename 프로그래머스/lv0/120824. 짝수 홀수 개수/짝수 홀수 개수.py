def solution(num_list):
    q, a = 0, 0
   
    for num in num_list:
        if num%2 == 0:
            a += 1
        else:
            q += 1

    return [a, q]