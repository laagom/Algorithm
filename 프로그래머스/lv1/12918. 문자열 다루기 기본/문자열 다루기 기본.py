def solution(s):
    answer = True
    length = len(s)
    if length in [4, 6]:
        for char in s:
            if char.isalpha():
                return False
    else:
        return False
    return answer