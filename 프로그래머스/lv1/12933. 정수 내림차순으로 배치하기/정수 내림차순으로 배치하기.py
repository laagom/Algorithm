def solution(n):
    arr = []
    while n >= 1:
        arr.append(str(n%10))
        n //= 10
    arr.sort(reverse=True)
    return int(''.join(arr))