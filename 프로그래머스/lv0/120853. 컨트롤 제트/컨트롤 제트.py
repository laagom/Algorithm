def solution(s):
    answer = []

    for element in s.split(' '):
        if element != 'Z':
            answer.append(int(element))
        else:
            answer.pop()
    
    return sum(answer)