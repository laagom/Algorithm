import sys
number = int(sys.stdin.readline())
list_A = list(map(int, sys.stdin.readline().split()))

nge =  [-1]*number
index = []

for i in range(number):
    while index and list_A[index[-1]] < list_A[i]:
        nge[index[-1]] = list_A[i]
        index.pop()
    index.append(i)
print(*nge)