import numpy

def solution(arr):
    a = numpy.array(arr)  
    indexs = numpy.where(a==2)[0]
     
    return arr[indexs[0]:indexs[-1]+1] if 2 in arr else [-1]