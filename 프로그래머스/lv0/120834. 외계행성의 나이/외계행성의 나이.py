def solution(age):
    alpha_age = ['a','b','c','d','e','f','g','h','i','j']
    answer = ''  

    for num in str(age):
        answer += alpha_age[int(num)]
    return answer