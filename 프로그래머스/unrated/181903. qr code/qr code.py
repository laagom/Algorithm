def solution(q, r, code):
    return ''.join(char for i, char in enumerate(code) if int(i%q) == r)