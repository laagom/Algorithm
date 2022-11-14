def solution(sides):
    temp = sorted(sides, reverse=True)
    
    if temp[0] < temp[1] + temp[2]:
        return 1
    else:
        return 2