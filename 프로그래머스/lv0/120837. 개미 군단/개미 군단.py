def solution(hp):
    장군개미 = 5
    병정개미 = 3
    일개미 = 1
    
    # 23/5 => (4, 3)  3/3 => (1, 0)
    # 24/5 => (4, 4)  4/3 => (1, 1)  1/1 => (1, 0)
    
    anti = 0
    
    while(hp > 0):
        if hp >= 장군개미:
            anti += hp//장군개미
            hp = hp%장군개미
        
        elif hp >= 병정개미:
            anti += hp//병정개미
            hp = hp%병정개미
            
        elif hp >= 일개미:
            anti += hp//일개미
            hp = hp%일개미
     
    return anti