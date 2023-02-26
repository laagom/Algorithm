def solution(participant, completion): 
    players = {}
    
    # 경기에 참가한 선수들을 dictionary에 할당
    # 동명이 있을 수 있게 때문에 선수의 수는 2이상이 될 수 있다.
    for person in participant:
        if person in players.keys():    
            players[person] += 1
        else:
            players[person] = 1
    
    # 경기에 완료한 선수들을 차감
    # 결과적으로 1이 남는 선수가 완료하지 못한 선수가 됨
    for person in completion:
        players[person] += -1
    
    # 결과가 1이 남는 선수의 이름을 반환
    return ''.join([person for person, count in players.items() if count == 1])