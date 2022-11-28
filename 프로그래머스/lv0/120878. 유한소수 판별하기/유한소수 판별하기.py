def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2


# 최대공약수
def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a%i == 0 and b%i ==0:
            return i
