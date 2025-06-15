def solution(s):
    
    stack = []
    
    for sign in s:
        # 열린괄호
        if sign == "(":
            stack.append(sign)
        else:
            # 닫힌괄호
            if stack:
                stack.pop()
            else:
                return False
        # print(stack)
    if stack:
        return False

    return True