def solution(a, b):
    
    # 앞에서 사용한 zip이용하여 x와 y를 매핑해준 후 x*y값을 출력하여 sum해줌     
    answer = sum([x*y for x,y in zip(a,b)])
    return answer