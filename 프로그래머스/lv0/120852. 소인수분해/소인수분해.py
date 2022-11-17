def solution(n):
    answer = []
    q=[]
    for i in range(2,n+1):   #n의 약수 구하기
        if n%i ==0:
            q.append(i)    

    for i in q:  #n의 약수 중에서 소수 구하기
        for j in range(2,5000):
            if i*j in q:
                q.remove(i*j)
    q.sort()
    return q