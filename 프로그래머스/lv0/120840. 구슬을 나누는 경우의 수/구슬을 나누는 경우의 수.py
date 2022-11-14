import math
def factorial(n):
    result = 1
    for item in range(1, n+1, 1):
        result *= item 
    return result


def solution(balls, share):
    answer = ''    
    answer = factorial(balls)/((factorial(balls-share))*factorial(share))
      
    return answer