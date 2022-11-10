def solution(n):
    pizza_piece = 6
    people = n
    
    pizza = 1
    while (pizza_piece * pizza) % n != 0:
        pizza += 1

    return pizza