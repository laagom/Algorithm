def solution(myString, pat):
    myString = list(myString)
    for i in range(len(myString)-1, -1, -1):
        string = myString[:i+1]
        if ''.join(string).endswith(pat):
            return ''.join(string)