from collections import deque
def solution(numbers, direction):
    # "left" = [1, 2, 3] -> [2, 3] -> [2, 3, 1]
    # "right" = [1, 2, 3] -> [1, 2] -> [3, 1, 2]
    numbers = deque(numbers)
    
    numbers.insert(0, numbers.pop()) if direction == 'right' else numbers.append(numbers.popleft())
        
        
    return list(numbers)