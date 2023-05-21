def solution(participant, completion):   
    participant_count = {}
    for person in participant:
        if person in participant_count.keys():
            participant_count[person] += 1
        else:
            participant_count[person] = 1
    
    for person in completion:
        participant_count[person] -= 1
    
    participant_count = {key:value for key, value in participant_count.items() if value != 0}

    return ''.join(list(participant_count.keys()))