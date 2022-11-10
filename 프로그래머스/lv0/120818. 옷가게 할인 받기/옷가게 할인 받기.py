
def solution(price):
    
    discout = {500000 : 0.8, 300000 : 0.9, 100000 : 0.95}
    
    for base, cnt in discout.items():
        if price >= base:
            return int(price* cnt)
    return price
 