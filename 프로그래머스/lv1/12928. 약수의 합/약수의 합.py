def solution(n):
    return n + sum([num for num in range(1, (n//2)+1) if n%num == 0])