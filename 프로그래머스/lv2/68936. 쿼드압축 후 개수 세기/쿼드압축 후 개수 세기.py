
def solution(arr):
    global answer
    answer = [0, 0]
    check(arr, len(arr), 0, 0)
    return answer

def check(arr, length, x, y):
 
    check_value = arr[y][x]
    for i in range(length):
        for j in range(length):
            if check_value != arr[y+i][x+j]:
                length //= 2
                check(arr, length, x, y)
                check(arr, length, x+length, y)
                check(arr, length, x, y+length)
                check(arr, length, x+length, y+length)
                return
   
    answer[check_value] += 1
