def solution(n, control):
    answer = n
    hash_map = {"w": 1, "s": -1, "d": 10, "a": -10}
    
    for str in control:
        answer += hash_map[str]
    return answer