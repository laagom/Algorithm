def solution(s):
    answer = 0
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
    if len(stack) == 0:
        answer = 1
    return answer

s = " aaaaa "
print(solution(s))