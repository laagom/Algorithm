def solution(numbers, k):
    answer = 0
    
    cnt = 0
    while True:
        cnt += 1
        
        if k == cnt:
            if k <= len(numbers):
                return numbers[cnt-1]
            else:
                return numbers[cnt-1]
        
        
    
    return answer