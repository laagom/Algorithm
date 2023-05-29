def solution(t, p):
    arr = []
    length = len(p)
    for i, char in enumerate(t):
        char = t[i:i+length]
        # 슬라이싱으로 추출한 길이가 p의 길이 and p의 값보다 작은
        if len(char) == length and char <= p:
            arr.append(char)
    return len(arr)

print(solution("123456", "10"))