def solution(x):
    hashad_number = x
    sum_x = 0
    
    while x > 0:
        sum_x += x%10
        x //= 10
        
    return True if hashad_number%sum_x == 0 else False