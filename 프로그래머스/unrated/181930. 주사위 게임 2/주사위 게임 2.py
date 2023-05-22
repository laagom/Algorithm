def solution(a, b, c):
    point = 0
    if a != b and b != c and c != a:
        point = a+b+c
    elif a == b and b == c and b == c:
        point = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    else:
        point = (a+b+c)*(a**2+b**2+c**2)
          
    return point