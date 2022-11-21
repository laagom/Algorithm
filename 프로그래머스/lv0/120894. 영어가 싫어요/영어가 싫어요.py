def solution(numbers):
    answer = ''
    temp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    temp_char = ''
    for char in numbers:
        temp_char += char
        
        if temp_char in temp:
            answer += str(temp.index(temp_char))
            temp_char = ''

    return int(answer)