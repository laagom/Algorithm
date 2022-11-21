def solution(numbers):
    answer = 0
    
    temp = sorted(numbers)
    print(sorted(numbers))
    
    if temp[0]*temp[1] > temp[-1]*temp[-2]:
        return temp[0]*temp[1]
    else:
        return temp[-1]*temp[-2]
