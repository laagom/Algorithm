def solution(n, k):
    answer = ''
    service_qty = 10
    food_price = 12000
    drink_price = 2000
    
    print(n//service_qty)
    
    answer = food_price*n + drink_price*k -(n//service_qty)*drink_price

    return answer