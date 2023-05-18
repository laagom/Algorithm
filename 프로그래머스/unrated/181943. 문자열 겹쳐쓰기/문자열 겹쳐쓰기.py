def solution(my_string, overwrite_string, s):
    my_string = list(my_string)   
    for i in range(len(overwrite_string)):
        for j, str in enumerate(my_string):
            if i+s == j:
                my_string[j] = overwrite_string[i]
    return ''.join(my_string)