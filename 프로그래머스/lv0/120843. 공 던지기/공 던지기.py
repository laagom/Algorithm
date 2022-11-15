def solution(numbers, k):
    answer = 0   
    index  = 0
    
    for i in range(k):
        answer = numbers[index]
        index += 2
        
        if index >= len(numbers):
            index -= len(numbers)
            
    return answer