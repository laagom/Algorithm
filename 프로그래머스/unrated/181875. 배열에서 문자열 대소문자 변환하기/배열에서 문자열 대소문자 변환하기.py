def solution(strArr):
    for i, string in enumerate(strArr):
        if i%2 == 0:
            strArr[i] = string.lower()
        else:
            strArr[i] = string.upper()
    return strArr