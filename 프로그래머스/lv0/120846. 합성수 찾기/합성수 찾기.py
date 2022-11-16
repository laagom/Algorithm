def solution(n):
    cnt = 0
    
    for i in range(1, n+1):
        if test(i):
            cnt += 1
        
    return cnt

def test(num):
    cnt = 0
    
    for i in range(1, num+1):
        if num%i == 0:
            cnt += 1   
    return True if cnt >= 3 else False
        