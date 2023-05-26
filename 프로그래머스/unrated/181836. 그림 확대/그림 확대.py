def solution(picture, k):
    answer = []
    
    for pixel in picture:
        convert = ""
        for char in pixel:
            convert += char*k
        
        for _ in range(k):
            answer.append(convert)
    
    for pixel in answer:
        print(pixel)
    
    return answer