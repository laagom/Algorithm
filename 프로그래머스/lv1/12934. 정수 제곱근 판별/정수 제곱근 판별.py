def solution(n):
    num = pow(n,0.5)
    return pow(num+1,2) if num == int(num) else -1