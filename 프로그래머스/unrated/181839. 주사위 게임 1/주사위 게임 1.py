def solution(a, b):  
    return getPoint(a, b)


def getPoint(a, b):
    point = 0
    if a%2 == 1 and b%2 ==1:
        point = a**2+b**2
    elif a%2 == 1 or b%2 ==1:
        point = 2*(a+b)
    else:
        point = abs(a-b)
    return point