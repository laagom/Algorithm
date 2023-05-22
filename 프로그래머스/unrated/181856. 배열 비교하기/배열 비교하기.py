def solution(arr1, arr2):
    answer = 0
    arr1_length = len(arr1)
    arr2_length = len(arr2)
    
    if arr1_length > arr2_length:
        return 1
    if arr1_length < arr2_length:
        return -1
    if arr1_length == arr2_length:
        arr1_sum = sum(arr1)
        arr2_sum = sum(arr2)
        
        if arr1_sum > arr2_sum:
            return 1
        elif arr1_sum < arr2_sum:
            return -1
        else:
            return 0
        
    