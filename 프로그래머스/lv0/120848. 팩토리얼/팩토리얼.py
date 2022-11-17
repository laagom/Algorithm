def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        if n >= factorial(i):
            answer = i
            continue
        else:
            break
        
    return answer

def factorial(num):
    
    if num > 1:
        return num * factorial(num-1)
    return num
        