import heapq
def solution(scville, K):
    answer = 0
    
    # 스코빌을 heap 형태의 리스트로 변경
    heapq. heapify(scville)
    
    # 스코빌이 남아있을 때 까지 
    while len(scville) > 1:
        # 최소값을 추출
        min_ = heapq.heappop(scville)
        
        # 최소값 추출 시 K보다 이상인 경우 모든 음식이 스코빌 지수 K이상 이므로
        # return answer
        if min_ >= K:
            return answer
        
        # 만약, 그렇지 않다면 다음 최소값을 추출 후
        # 섞은 음식의 스코빌 지수 = 최소 스코빌 + (최소 다음 스코빌*2)
        # answer +1
        min_next = heapq.heappop(scville)
        heapq.heappush(scville, min_ + min_next*2)
        answer += 1
    
    if scville[0] <= K:
        return -1
    else:
        return answer