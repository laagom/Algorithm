import copy
def solution(arr):    
    count = 0
    pre_arr = []
    sub_arr = []
    
    while True:
        pre_arr = copy.copy(arr)
        for i, num in enumerate(arr):
            if num >= 50 and num%2 == 0:
                arr[i] = int(arr[i]/2)
            elif num < 50 and num%2 == 1:
                arr[i] = arr[i]*2 +1
        sub_arr = copy.copy(arr)
        count += 1
        
        if pre_arr == sub_arr:
            return count-1
    
    
        
        