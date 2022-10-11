def solution(grid):
    answer = []
    # 그리드의 길이 r, c
    # [S, L] 
    # [L, R]
    # => 2행 2열
    r, v = len(grid), len(grid[0])
    
    # 방문 여부
    visit = [[[] for _ in range(v)] for _ in range(r)]
    
    # 방향
    # x 축은 좌우 로 +,- 되기 때문에 위 아래로 이동하는 값은 0
    # y 축은 위아래로 +,- 되기 때문에 좌우로 이동하는 값은 0
    directions = {'U':[1,0], 'R':[0,1], 'D':[-1,0], 'L':[0,-1]}
    
    # x, y, ULDR(방향) 3중 반복문
    for x in range(r):       
        for y in range(v):            
            # 내가 지정해서 시작하는 위치는 0행 0열에서 UP(위로) 시작이다.
            for d in 'ULDR':
                # 움직이는 거리
                move = 0          
                while True:
                    # print(visit)
                    # while 정지를 위한 조건 추가
                    if d in visit[x][y]: 
                        break
                        
                    # 게시글(방문)추가    
                    visit[x][y].append(d)
                    move += 1
                    
                    # gird영역 밖을 넘어가는 경우 계산 하여 지정
                    x = (x + directions[d][1]) % r
                    y = (y + directions[d][0]) % v
                    
                    # 도착지점이 L인 경우
                    if grid[x][y] == 'L':
                        # L이란 녀석은 up -> left -> down -> right 순으로 감
                        idx = 'ULDR'.index(d)
                        d = 'ULDR'[0] if idx == 3 else 'ULDR'[idx+1]
                        
                    # 도착지점이 R인 경우
                    elif grid[x][y] == 'R':
                        # R이란 녀석은 up -> right -> down ->left 순으로 감
                        idx = 'URDL'.index(d)
                        d = 'URDL'[0] if idx == 3 else 'URDL'[idx+1]
                
                # 한 그리드당 이동 거리 추가
                if move > 0 : answer.append(move)

    return sorted(answer)