def solution(babbling):
    answer = 0
    can_char = ["aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        for check in can_char:
            
            if check in babbling[i]:
                babbling[i] = babbling[i].replace(check, ' ')
                
    return [char.replace(' ','') for char in babbling].count('')