def solution(strArr):
    remove_word = "ad" 
    return [word for word in strArr if remove_word not in word]