def solution(arr):
    answer = []

    # 임의 변수 -1 설정,배열 요소와 비교
    front = -1

    for item in arr:
        if front != item:
            front = item
            answer.append(item)   
    return answer

    # return [s[i] for i in range(len(s)) if s[i] != s[i+1:i+2]]
arr = [1, 1, 3, 3, 0, 1, 1]
solution(arr)