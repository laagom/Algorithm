def solution(array, n):
    temp = []
    
    print(sorted(array))
    
    for num in sorted(array):
        if num >= n:
            temp.append(num-n)
        elif num < n:
            temp.append(n-num)
            
    return sorted(array)[temp.index(min(temp))]