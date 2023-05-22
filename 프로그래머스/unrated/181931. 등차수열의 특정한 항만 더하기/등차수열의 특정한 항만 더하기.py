def solution(a, d, included):
    answer = 0
    
    for i, boolean in enumerate(included):
        if boolean:
            answer += a+(i*d)
    return answer