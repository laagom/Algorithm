# 1번 최소직사각형

def solution(sizes):
    max_w = 0
    max_h = 0

    for s in sizes:
        s.sort()
        max_w = max(max_w,s[0])
        max_h = max(max_h,s[1])

    return max_w * max_h

solution([[60, 50], [30, 70], [60, 30], [80, 40]])