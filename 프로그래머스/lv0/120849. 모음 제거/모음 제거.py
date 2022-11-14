def solution(my_string):
    mo = ['a', 'e', 'i', 'o', 'u']      
    return ''.join([char for char in my_string if char not in mo]) 