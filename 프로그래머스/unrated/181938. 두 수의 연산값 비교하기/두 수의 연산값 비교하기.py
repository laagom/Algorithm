def solution(a, b):
    calc_value = calc(a, b)
    formula = 2*a*b
    return calc_value if calc_value >= formula else formula

def calc(a, b):
    pre = int(str(a) + str(b))
    return pre