def solution(board, k):
    answer = 0
    for i, num_list in enumerate(board):
        for j, num in enumerate(num_list):
            if i+j <= k:
                answer += num
    return answer