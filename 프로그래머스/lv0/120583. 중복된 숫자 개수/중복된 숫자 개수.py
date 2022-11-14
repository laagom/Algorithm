def solution(array, n):
    answer = 0
    temp = [0]*(max(array)+1)
    
    for num in array:
        temp[num] += 1

    return temp[n]