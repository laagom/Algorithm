def solution(foods):
    answer = ''
    for i, food in enumerate(foods[1:], 1):
        answer += str(i)*(int(food//2))
    answer += "0" + answer[::-1] 
    return answer