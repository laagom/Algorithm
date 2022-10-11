def solution(absolutes, signs):
    answer = 0
    
    # 풀이 1     
    # for i in range(len(signs)):
    #     if signs[i]:
    #         answer += absolutes[i] 
    #     else:
    #         answer -= absolutes[i] 
    
    # 풀이 2       
    # zip 사용 풀이 : 두개의 서로다른 배열의 위치를 그룹화 해주는 모듈 함수     
    for absolutes, sign in zip(absolutes, signs):
        
        answer += absolutes if sign else -absolutes
    
    return answer