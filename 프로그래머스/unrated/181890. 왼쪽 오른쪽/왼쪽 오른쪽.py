def solution(str_list):
    if 'l' not in str_list and 'r' not in str_list:
        return []
    
    for i, char in enumerate(str_list):
        if char == 'l':
            return str_list[:i]
        elif char == 'r':
            return str_list[i + 1:]
    else:
        return str_list