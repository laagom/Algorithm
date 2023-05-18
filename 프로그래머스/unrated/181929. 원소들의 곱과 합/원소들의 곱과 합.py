from functools import reduce
def solution(num_list):
    amount = (sum(num_list))**2
    multi = reduce(lambda x, y: x*y, num_list)
    return 1 if amount > multi else 0