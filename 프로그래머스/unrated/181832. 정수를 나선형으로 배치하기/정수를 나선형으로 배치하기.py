def solution(n):
    if n == 1:
        return [[1]]
    direction = {'r': [0, 1], 'd': [1, 0], 'l': [0, -1], 'u': [-1, 0]}
    
    answer = [[0]*n for i in range(n)]
    x = 0
    y = 0
    dir = 'r'
    
    for i in range(1, n**2+1):
        answer[x][y] = i
        if dir == 'r':
            if y == n-1 or answer[x][y+1] != 0:
                dir = 'd'
        elif dir == 'd':
            if x == n-1 or answer[x+1][y] != 0:
                dir = 'l'
        elif dir == 'l':
            if y == 0 or answer[x][y-1] != 0:
                dir = 'u'
        elif dir == 'u':
            if x == n-1 or answer[x-1][y] != 0:
                dir = 'r'
        x += direction[dir][0]
        y += direction[dir][1]
                
    return answer