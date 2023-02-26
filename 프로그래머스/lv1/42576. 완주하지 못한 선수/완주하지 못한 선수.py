def solution(participant, completion):
    
    players = {}
    
    for people in participant:
        if people in players.keys():    
            players[people] += 1
        else:
            players[people] = 1
            
    for player in completion:
        players[player] += -1
        
    return ''.join([player for player, count in players.items() if count == 1])