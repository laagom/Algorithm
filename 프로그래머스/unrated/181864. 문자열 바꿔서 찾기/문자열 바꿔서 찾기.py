def solution(myString, pat):
    answer = 0
    myString = list(myString)
    for i, char in enumerate(myString):
        myString[i] = "B" if char == "A" else "A"
    print(myString)
    
    if pat in ''.join(myString):
        return 1
    return answer