def solution(my_string):
    answer = []

    for num in range(ord('A'), ord('Z')+1):
        answer.append(my_string.count(chr(num)))
        
    for num in range(ord('a'), ord('z')+1):
        answer.append(my_string.count(chr(num)))

    return answer