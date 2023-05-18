def solution(my_string, overwrite_string, s):
    # 풀이 1: 2중 루프
    # my_string = list(my_string)   
    # for i in range(len(overwrite_string)):
    #     for j, str in enumerate(my_string):
    #         if i+s == j:
    #             my_string[j] = overwrite_string[i]
    # return ''.join(my_string)
    
    # 풀이 2: 슬라이싱
    return my_string[0:s] + overwrite_string + my_string[s+len(overwrite_string):]

    