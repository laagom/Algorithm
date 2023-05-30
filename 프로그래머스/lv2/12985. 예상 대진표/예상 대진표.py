# from collections import deque
# import random
# def solution(n,a,b):
#     arr = list(range(1, n+1))   
#     _round_ = 1
    
#     while len(arr) > 0:
#         win_arr = []      
#         # 라운드 시작
#         while len(arr) > 0:
#             temp = arr[0:2]
#             # a, b가 겨루지 않는 경기
#             if a not in temp and b not in temp:
#                 choice_number = random.choice(arr[0:2])
#             # a 만 포함된 경기
#             elif a in temp and b not in temp:
#                 choice_number = a 
#             # b 만 포함된 경기
#             elif a not in temp and b in temp:
#                 choice_number = b
#             # a, b 둘다 포함된 경기
#             elif a in temp and b in temp:
#                 return _round_
            
#             # 승자를 다른 배열에 담고 기존 배열에서 제외
#             win_arr.append(choice_number)
#             arr = arr[2:]
        
#         # 다음 라운드를 위한 초기화
#         _round_ += 1
#         arr = win_arr
#     return _round_

def solution(n,a,b):
    answer = 0
    while(a!=b):
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
    return answer

# 테스트 케이스
# print(solution(8, 4, 5))
# print(solution(2, 1, 2))