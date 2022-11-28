def solution(score):
    answer = []
    for i in range(len(score)):
        answer.append((score[i][0]+score[i][1])/len(score))
        
    return [sorted(answer,reverse=True).index(x)+1 for x in answer]