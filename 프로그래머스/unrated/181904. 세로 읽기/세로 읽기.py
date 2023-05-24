def solution(my_string, m, c):
    return ''.join([string for i, string in enumerate(my_string) if i%m == c-1])