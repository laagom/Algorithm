def solution(money):
    ice_americano = 5500
    
    cnt = 0
    while money >= ice_americano and money > 0:
        money -= ice_americano
        cnt += 1
        print(money)
    
    return [cnt, money]