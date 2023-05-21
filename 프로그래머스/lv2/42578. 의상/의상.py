def solution(clothes):
    answer = 1
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] not in clothes_dict:
            clothes_dict[cloth[1]] = 1
        else:
            clothes_dict[cloth[1]] += 1
    
    # (x+a)(x+b)(x+c) = x3 + (a+b+c)x2 + (ab+bc+ca)x + (abc)의 계산식
    for h in clothes_dict.values():
        answer = (h+1)*answer

    return answer-1