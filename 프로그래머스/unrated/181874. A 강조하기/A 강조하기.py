def solution(myString):
    myString = list(myString)
    for i, char in enumerate(myString):
        if char == "a":
            myString[i] = "A"
        elif char != "A":
            myString[i] = char.lower()
    return ''.join(myString)