def solution(dots):
    answer = 0
    
    #width = max() x값 - min() x값
    #heith = max() y값 - min() y값
    
    width = max([dot[0] for dot in dots])-min([dot[0] for dot in dots])

    
    height = max([dot[1] for dot in dots])-min([dot[1] for dot in dots])
          
    return width*height