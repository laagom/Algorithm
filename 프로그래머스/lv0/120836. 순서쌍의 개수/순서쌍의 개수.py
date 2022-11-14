def solution(n):
    answer = 0
    array = []
    # 20/1 20/2 20/3 20/4 20/5
    
    for i in range(1, n+1):
        if n%i == 0:
            array.append(i)
    print(array)
    
    return len(array)