# 2번. 모의고사

def solution(answers):
    
    li = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    answer = [0,0,0]
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == li[j][i%len(li[j])]:
                answer[j] += 1
    
    max_answer = max(answer)

    return [i+1 for i in range(3) if max_answer == answer[i]]

# solution([1,2,3,4,5])
# solution([1,3,2,4,2])