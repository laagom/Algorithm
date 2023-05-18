def solution(num_list):
    # oven = ''.join([str(num) for num in num_list if num%2 == 0])
    # odd = ''.join([str(num) for num in num_list if num%2 == 1])
    oven = ""
    odd = ""
    
    for num in num_list:
        if num%2 == 0:
            oven += str(num)
        else:
            odd += str(num)
    
    return int(oven) + int(odd) 