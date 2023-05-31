def solution(arr):
    lcm_num = 1
    for num in range(len(arr)):
        lcm_num = lcm(arr[num], lcm_num)
    return lcm_num

def gcd(n, m):   
    while m > 0:
        n, m = m, n%m
    return n

def lcm(n, m):
    return (n * m)//gcd(n, m)
    
    
    
