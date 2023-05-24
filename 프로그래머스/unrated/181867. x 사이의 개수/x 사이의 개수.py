def solution(myString):
    temp_string = myString.split('x')
     
    return [len(string) for string in temp_string]