def solution(n):
    answer = 0
    array = []
    
    for i in range(1, n+1):
        if n%i == 0:
            array.append(i)

    if len(array)%2 == 0:
        return 2
    else:
        return 1