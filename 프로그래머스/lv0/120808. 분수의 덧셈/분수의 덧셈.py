import math

def solution(denum1, num1, denum2, num2):
    # 프로그래머스에서 math모듈의 lcm 지원하지 않음
    top = denum1*num2 + denum2*num1
    bottom = num1*num2
    
    mid_num = math.gcd(top, bottom)
    
    if mid_num == 1:
        return [top, bottom]
    else:
        return [top/mid_num, bottom/mid_num]