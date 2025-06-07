def solution(n, k):
    yang = 12000 # 양꼬치
    drink = 2000 # 음료
    yang_price = 12000 * n # 양꼬치 주문 가격
    drink_price = 2000 * k # 음료 주문 가격
    service = (n//10) * 2000 # 서비스 가격
    
    # 총 지불 가격
    tot_price = yang_price + drink_price - service
    return tot_price