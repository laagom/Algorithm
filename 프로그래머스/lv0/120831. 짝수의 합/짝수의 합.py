def solution(n):
  
    return sum(filter(lambda x: x % 2 == 0, [_ for _ in range(n+1)]))
