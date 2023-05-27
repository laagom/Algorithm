def solution(a, b):
    if a > b:
        a, b = b, a
    if a == b:
        return a
    return sum([num for num in range(a, b+1)])