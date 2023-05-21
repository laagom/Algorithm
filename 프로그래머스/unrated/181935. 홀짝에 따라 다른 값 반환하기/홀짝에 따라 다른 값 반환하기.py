def solution(n):
    flag = True if n%2 == 0 else False

    return sum_oven(n) if flag else sum_odd(n)

def sum_odd(n):
    print('This id odd function!')
    odd_num = 0
    for num in range(n+1):
        if num%2 != 0:
            odd_num += num
    return odd_num
            
def sum_oven(n):
    print('This id oven function!')
    oven_num = 0
    for num in range(n+1):
        if num%2 == 0:
            oven_num += num**2
    return oven_num
