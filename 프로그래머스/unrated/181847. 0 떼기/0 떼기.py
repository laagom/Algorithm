def solution(n_str):
    n_str = list(n_str)
    temp_str = list(n_str)
    for i in range(0, len(n_str)):
        if temp_str[i] == "0":
            del n_str[0]
        else:
            break
    return ''.join(n_str)