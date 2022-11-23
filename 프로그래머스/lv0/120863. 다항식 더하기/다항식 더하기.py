def solution(polynomial):
    answer = ''
    
    temp  = polynomial.split(' ')
    x_num = 0
    num   = 0
    
    for char in temp:
        if 'x' in char and len(char) > 1:
            x_num += int(char.replace('x', ''))
        elif 'x' in char and len(char) == 1:
            x_num += 1
        elif char != '+':
            num += int(char)
    
    if x_num == 0 and num == 0:
        answer = '0'
    elif x_num == 0 and num != 0:
        answer = f'{num}'
    elif x_num != 0 and num == 0:
        answer = f'{x_num}x'
        if x_num == 1:
            answer = f'x'
    elif x_num != 0 and num != 0:
        answer = f'{x_num}x + {num}'
        if x_num == 1:
            answer = f'x + {num}'

    return answer