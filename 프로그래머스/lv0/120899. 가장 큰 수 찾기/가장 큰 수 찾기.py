def solution(array):  
    list = sorted(array)
    
    print(max(list))
    print(sorted(array).index(max(list))-1)
    
    
    return [list[-1], array.index(list[-1])]