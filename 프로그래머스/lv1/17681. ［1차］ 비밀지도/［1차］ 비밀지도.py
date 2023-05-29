def solution(n, arr1, arr2):
    answer, map1, map2 = [], [], []
    # 지도 1
    for num in arr1:
        convert_num = bin(num)[2:]
        if len(convert_num) < n:
            binary_num = list("0"*(n-len(convert_num)) + convert_num)
        else:
            binary_num = list(convert_num)
        map1.append(binary_num)
    
    # 지도 2
    for num in arr2:
        convert_num = bin(num)[2:]
        if len(convert_num) < n:
            binary_num = list("0"*(n-len(convert_num)) + convert_num)
        else:
            binary_num = list(convert_num)
        map2.append(binary_num)
    
    # 지도 1 + 지도 2
    for in_arr1, in_arr2 in zip(map1, map2): 
        temp = ""
        for num1, num2 in zip(in_arr1, in_arr2):
            if len(temp) <= n:
                wall = bool(int(num1)) or bool(int(num2))
                temp += "#" if wall else " "
        answer.append(temp)
    return answer