def solution(n):
    answer = 0
    
    # 풀이1
    # n 과 n+1 둘다 모두 정답이 되는데, n+1 : 어차피 n본인 자신이기 때문에 필요 X
    # for i in range(1, n):
    #     if n % i == 1:
    #         answer = i
    #         break
    # return answer     
    
    # 풀이2
    # 배열 안에서 조건문과 반복문 사용
    answer = [idx for idx in range(1,n+1) if n%idx==1][0]
    return answer         