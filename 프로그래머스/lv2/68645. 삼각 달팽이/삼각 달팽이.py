# from itertools import chain

# def solution(n):
    
#     li = [[0 for j in range(i+1)] for i in range(n)]
#     x, y = 0, -1
#     value = 1
#     direction = 0
#     move = [[1, 0], [0, 1], [-1, -1]]
#     length = n
    
#     while value <= sum(range(1, n+1)):
#         for i in range(length):
#             y += move[direction][0]
#             x += move[direction][1]
#             li[y][x] = value
#             value += 1      
#         direction = (direction + 1) % 3
#         length -= 1
    
#     answer = []
    
#     # for i in li:
#     #     answer.extend(i)
#     #     for j in j:
#     #         answer.append(j)
    
    
#     # return answer
#     return list(chain(*li))

from collections import deque
from itertools import chain

def solution(n):
    # 숫자를 담을 삼각형 구조의 2차원 배열을 생성
    # 모든 요소는 0으로 지정
    answer = [[0]* (i+1) for i in range(n)]

    # 방향을 표시할 덱 생성
    #    0 : 「좌하단으로 이동」을 의미
    #    1 : 「우측으로 이동」을 의미
    #    2 : 「좌상단으로 이동」을 의미
    check = deque([0,1,2])
    # 시작 지점을 지정
    #   x가 -1인 이유는, 무조건 제일 처음 시행 시 「좌하단으로 이동」(x += 1)하여 (0, 0)의 좌표로 이동하기 때문
    x , y = -1, 0
    # 해당 위치 좌표에 들어갈 값을 담을 변수를 num으로 지정
    num = 0
    # 총 n번의 방향으로 숫자를 넣어주게 됨
    for i in range(n):
        # 현재 방향에서 (n-i)개의 숫자를 삽입하는 과정을 반복
        for j in range(n-i):
            # 만약 「좌하단으로 이동」을 의미한다면
            if check[0] ==0:
                # x 좌표에 1을 늘려줌
                x += 1
            # 만약 「오른쪽으로 이동」을 의미한다면
            elif check[0] == 1:
                # y 좌표에 1을 늘려줌
                y += 1
            # 만약 「좌상단으로 이동」을 의미한다면
            else:
                # x, y 좌표에서 각각 1씩 줄여줌
                x -= 1
                y -= 1
            # 해당 좌표에 삽입할 숫자 값을 하나 증가시킴
            num += 1
            # (x, y) 좌표에 숫자를 삽입
            answer[x][y] = num
        # 현재 방향에서의 작업을 완료하였다면, 다음 방향으로 변경 
        check.rotate(-1)
    # 2차원 배열을 언패킹 후, 하나의 객체로 묶어준 후 리스트로 변환
    return list(chain(*answer))
