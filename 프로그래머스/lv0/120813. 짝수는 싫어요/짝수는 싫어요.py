def solution(n):  
    if 1 <= n and 100 >= n:
        answer = [i for i in range(n+1) if i%2 == 1]
        
    return answer