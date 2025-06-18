def solution(numbers):
    temp = sorted(numbers, reverse=True)
    return temp[0]*temp[1]