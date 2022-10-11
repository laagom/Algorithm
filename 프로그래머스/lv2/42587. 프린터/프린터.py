def solution(priorities, location):
    answer = 0
    
    # A B C D (2 번째)
    # 2 1 3 2 -> C D A B
    
    # A B C D E F (0 번째)
    # 1 1 9 1 1 1 -> C D E F A B
    
    while True:
        # 최대값
        max_num = max(priorities)
        print(f'max_num : {max_num}')
        
        for i in range(len(priorities)):        
            # 최대값이 일치하면
            if max_num == priorities[i]:
                
                # 해당 답에 대한 순위 +1
                answer += 1
                
                # 최대값을 찾는 순위에서 제외
                priorities[i] = 0
                print(priorities)
                
                # 최대값을 다시 구함
                max_num = max(priorities)
                print(f'max_num : {max_num}')
                print(f'answer : {answer}')
                
                # i와 위치와 일치하면 answer 반환
                if i == location:
                    return answer
                