def solution(num_list):
    oven = ''.join([str(num) for num in num_list if num%2 == 0])
    odd = ''.join([str(num) for num in num_list if num%2 == 1])
    return int(oven) + int(odd)