def solution(numbers, n):
    amount = 0
    for num in numbers:
        amount += num
        if amount > n:
            return amount