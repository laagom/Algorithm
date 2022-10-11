n = int(input())

for _ in range(n):
    str = list(input())

    stack = []
    flag = False

    for chr in str:
        if chr == "(":
            stack.append(chr)
        else:
            if len(stack) == 0:
                flag = True
                break
            stack.pop()
            
    print("NO") if flag or len(stack) > 0 else print("YES")