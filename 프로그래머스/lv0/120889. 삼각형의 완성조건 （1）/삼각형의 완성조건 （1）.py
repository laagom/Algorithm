def solution(sides):
    temp = sorted(sides, reverse=True)
    return 1 if temp[0] < temp[1] + temp[2] else 2