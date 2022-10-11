import sys 
from collections import deque

n = int(sys.stdin.readline())
deq = deque()

for i in range(n):
    text = sys.stdin.readline().strip() 

    if text.split()[0] == 'push_front':
        deq.appendleft(text.split()[1])

    elif text.split()[0] == 'push_back':
        deq.append(text.split()[1])

    elif text == 'pop_front':
        print( deq.popleft() if deq else -1)

    elif text == 'pop_back':
        print( deq.pop() if deq else -1)

    elif text == 'size':
        print(len(deq))

    elif text == 'empty':
        print( 0 if deq else 1)

    elif text == 'front':
        print( deq[0] if deq else -1)

    elif text == 'back':
        print( deq[-1] if deq else -1)