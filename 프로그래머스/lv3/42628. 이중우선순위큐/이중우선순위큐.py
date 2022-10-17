import heapq
def solution(arguments):
    heap = []
    
    for operation in arguments:
        op, num = operation.split() # operation 앞 뒤 부분으로 분리
        num = int(num)
        # heapq.heapify(heap)
        
        if op == "I": # 앞부분이 I인 경우 
            # print(f'heap : {heap}')
            heapq.heappush(heap, num)
            # print(f'after heap: {heap}')
        elif op == "D": # 앞부분이 D인 경우
            if num == 1:
                # print(f'heap : {heap}')
                # print(f'nlargest : {heapq.nlargest(1, heap)}')
                #heapq.heappop(heapq.nlargest(1,heap)) # heap의 최대값을 지우기
                heap = heapq.nlargest(len(heap), heap)[1:]
                # print(f'after heap : {heap}')
            else:
                # print(f'heap : {heap}')
                # print(f'nsmallest : {heapq.nsmallest(1, heap)}')
                # heapq.heappop(heap) # heap의 최소값을 지우기
                heap = heapq.nsmallest(len(heap), heap)[1:]
                # print(f'after heap : {heap}')
          
    if not heap: # heap의 데이터가 없으면
        return [0, 0]   
    
    return [max(heap), min(heap)]
