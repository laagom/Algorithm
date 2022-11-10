def solution(slice, n):
    pizza_piece = slice
    people = n
    
    remains = n % pizza_piece
    pizza = n // pizza_piece
     
    if remains < slice and remains != 0:
        pizza += 1
    return pizza