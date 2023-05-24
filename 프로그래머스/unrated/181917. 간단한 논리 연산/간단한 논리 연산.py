def solution(x1, x2, x3, x4):
    # ∨: True가 하나라도 있으면 True
    # ∧: False가 하나라도 있으면 False
    
    res1 = True if x1 == True or x2 == True else False
    res2 = True if x3 == True or x4 == True else False
    res3 = False if res1 == False or res2 == False else True
 
    return res3