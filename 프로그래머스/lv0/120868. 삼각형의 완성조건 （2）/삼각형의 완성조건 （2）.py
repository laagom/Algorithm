def solution(sides):
    # [11, 7]
    #sides[0], sides[1] => sides[0]

    return (sides[1]*2 -1) if sides[0] > sides[1] else (sides[0]*2 -1)