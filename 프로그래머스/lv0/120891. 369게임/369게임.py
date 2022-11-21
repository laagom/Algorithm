def solution(order):
    answer = 0
    temp = ['3', '6', '9']
    
    for num in str(order):
        if num in temp:
            answer += 1
        
    return answer