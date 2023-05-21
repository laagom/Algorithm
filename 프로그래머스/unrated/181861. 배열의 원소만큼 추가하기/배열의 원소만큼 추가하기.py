def solution(arr):
    temp = []
    for x in arr:
        print(x)
        for __ in range(int(x)):
            temp.append(x)
    return temp