# def solution(keyinput, board):
#     answer = [0, 0]
    
#     arrow = {'up':[0,1], 'down':[0,-1], 'right':[1,0], 'left':[-1,0]}
        
#     for key in keyinput:
        
#         answer[0] += arrow[key][0]
#         answer[1] += arrow[key][1] 

#     if answer[0] > 0 and answer[0] > (board[0]-1)//2:
#         answer[0] = (board[0]-1)//2
        
#     elif answer[0] < 0 and answer[0] < -((board[0]-1)//2)
#         answer[0] = -((board[0]-1)//2)

#     if answer[1] > 0 and answer[1] > (board[1]-1)//2:
#         answer[1] = (board[1]-1)//2
        
#     elif answer[1] < 0 and answer[1] < -((board[1]-1)//2)
#         answer[1] = -((board[1]-1)//2)
            
#     return answer

def solution(keyinput, board):
    col = board[0]
    row = board[1]
    result = [0, 0]
    
    for i in keyinput:
        if i == "left" and result[0]-1 >= -(col // 2):
            result[0] -= 1
        elif i == "right" and result[0]+1 <= (col // 2):
            result[0] += 1
        elif i == "up" and result[1]+1 <= (row // 2):
            result[1] += 1
        elif i == "down" and result[1]-1 >= -(row // 2):
            result[1] -= 1
    return result