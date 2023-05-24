def solution(myString):
    temp_string = myString.split("x")    
    temp_string.sort()

    return [string for string in temp_string if string != ""]