def solution(s):
    number = {
        "zero": 0, "one": 1, "two": 2,
        "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8,
        "nine": 9
    }
    string =""
    result = []
    for char in s:
        if char.isalpha():
            string += char
        else:
            result.append(int(char))
            
        if string in number:
            result.append(number[string])
            string =""
            
    return int(''.join(list(map(str, result))))