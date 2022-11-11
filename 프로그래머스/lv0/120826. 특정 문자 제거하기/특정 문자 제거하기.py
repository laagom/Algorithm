def solution(my_string, letter):
    array = [char for char in my_string if char != letter]
    
    return ''.join(array)