def solution(my_string):
    answer = []

    for char in list(my_string):
        if char not in answer:
            answer.append(char)
    
    return ''.join(answer)