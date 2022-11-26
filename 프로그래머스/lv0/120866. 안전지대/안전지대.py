# import numpy as np

# def solution(board):
#     answer = 0   
#     # [0, 0, 0, 0, 0]
#     # [0, 0, 0, 0, 0]
#     # [0, 0, 0, 0, 0]
#     # [0, 0, 1, 0, 0]
#     # [0, 0, 0, 0, 0]
    
#     # board[3][3] => [3][2] [3][4] [2][3] [4][3]
    
#     board = np.array(board)
#         for a, b in zip(*np.where(board == 1)):
#             board[a-1 if a else 0:a+2, b-1 if b else 0:b+2] = 1
#     return len(board[board == 0])

import numpy as np
def solution(board):
    board = np.array(board)
    for a, b in zip(*np.where(board == 1)):
        board[a-1 if a else 0:a+2, b-1 if b else 0:b+2] = 1
    return len(board[board == 0])