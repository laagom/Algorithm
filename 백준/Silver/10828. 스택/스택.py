import sys
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n) :
    order = list(input().split())
    if len(order) == 2 : # push X 일경우
        insert_value = int(order[1])
        q.append(insert_value)
        continue
    if order[0] == 'pop' :
        if len(q) == 0 : # 스택에 들어있는 정수가 없는 경우
            print(-1)
        else :
            pop_value = q.pop()
            print(pop_value)
    elif order[0] == 'size' :
        print(len(q))
    elif order[0] == 'empty' :
        if len(q) == 0 :
            print(1)
        else :
            print(0)
    elif order[0] == 'top' :
        if len(q) == 0 :
            print(-1)
        else :
            value = q[-1]
            print(value)