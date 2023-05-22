def solution(a, b, c):
    point = 0
    if a != b and b != c and c != a:
        print(1)
        point = a+b+c
    elif a == b and b == c and b == c:
        print(3)
        point = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    else:
        print(2)
        point = (a+b+c)*(a**2+b**2+c**2)
          
    return point