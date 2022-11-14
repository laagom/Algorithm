def solution(n):
    return 2 if len([i for i in range(1, n+1) if n%i == 0])%2 == 0 else 1