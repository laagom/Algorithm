def solution(n):
    pizza_piece = 7
    people = n
    
    answer = n // pizza_piece
    
    if n % pizza_piece < 7 and  n % pizza_piece != 0:
        answer += 1
    
    return answer