def solution(numbers):
    result = 0
    for num in numbers:
        result += num
    
    return result / len(numbers)