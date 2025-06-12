def solution(n):
    result = list(filter(lambda x: x%2 ==0, [_ for _ in range(n+1)]))
    return sum(result)
