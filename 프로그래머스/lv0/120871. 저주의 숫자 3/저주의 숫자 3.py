
def solution(n):
    temp_num = 0
    
    for num in range(1, n+1):
        temp_num += 1
        
        while(temp_num%3 == 0 or '3' in str(temp_num)):
            temp_num += 1
            
    return temp_num