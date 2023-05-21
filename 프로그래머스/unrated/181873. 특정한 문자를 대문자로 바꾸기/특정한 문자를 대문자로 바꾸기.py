def solution(my_string, alp):
    my_string = list(my_string)
    for i, string in enumerate(my_string):
        if string == alp:
            my_string[i] = string.upper()
    return ''.join(my_string)
        