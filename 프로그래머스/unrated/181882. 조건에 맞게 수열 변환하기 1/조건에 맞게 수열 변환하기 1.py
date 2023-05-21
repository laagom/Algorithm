def solution(arr):
    for i, element in enumerate(arr):
        if element >= 50 and element%2 == 0:
            arr[i] = int(element/2)
        elif element < 50 and element%2 == 1:
            arr[i] = element*2
    return arr