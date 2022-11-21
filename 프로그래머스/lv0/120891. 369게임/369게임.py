def solution(order):
    return len([1 for num in str(order) if num in ['3', '6', '9']])