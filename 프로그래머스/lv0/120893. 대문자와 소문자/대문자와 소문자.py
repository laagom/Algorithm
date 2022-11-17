def solution(my_string):
    answer = ''
    print(my_string.upper())
    
    for char in list(my_string):
        if char.isupper():
            answer += char.lower()
        else:
            answer += char.upper()
    return answer