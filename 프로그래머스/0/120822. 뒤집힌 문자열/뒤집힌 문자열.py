def solution(my_string):    
    answer = []

    array = [char for char in my_string]
    for _ in range(0, len(array)):
        answer.append(array.pop());
    
    return ''.join(answer)