# def solution(arr1, arr2):
#     answer = []
#     for d_arr1, d_arr2 in zip(arr1, arr2):
#         temp = []
#         for num1, num2 in zip(d_arr1, d_arr2):
#             temp.append(num1+num2)
#         answer.append(temp)
#     return answer

import numpy as np
def solution(arr1, arr2):
    answer = []
    
    numpy_arry1 = np.array(arr1)
    numpy_arry2 = np.array(arr2)
    answer = numpy_arry1 + numpy_arry2
    return answer.tolist()