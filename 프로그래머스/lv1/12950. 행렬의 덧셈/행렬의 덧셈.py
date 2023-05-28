def solution(arr1, arr2):
    answer = []
    for d_arr1, d_arr2 in zip(arr1, arr2):
        temp = []
        for num1, num2 in zip(d_arr1, d_arr2):
            temp.append(num1+num2)
        answer.append(temp)
    return answer