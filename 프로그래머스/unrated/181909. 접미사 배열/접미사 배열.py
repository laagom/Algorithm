def solution(my_string):
    answer = []
    my_string = list(my_string)
    for i in range(len(my_string)):
        answer.append(''.join(my_string[i:]))
    answer.sort()
    
    return answer