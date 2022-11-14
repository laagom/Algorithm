def solution(array, height):
    answer = []    
    return len([people for people in array if height < people])