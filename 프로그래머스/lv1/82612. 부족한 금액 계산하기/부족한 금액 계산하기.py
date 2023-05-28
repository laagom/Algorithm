def solution(price, money, count):
    amount = sum([price*num for num in range(1, count+1)])
    return amount-money if amount > money else 0