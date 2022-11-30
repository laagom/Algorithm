def solution(before, after):
    answer = 0
    
    for char1 in before:
        if char1 in after:
            after = after.replace(char1, '', 1)

    return 1 if after == '' else 0