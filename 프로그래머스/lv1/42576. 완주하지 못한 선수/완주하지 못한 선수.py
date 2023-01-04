def solution(participant, completion):
    answer = ''
    participant_dict = dict()
    
    for person in participant:
        if person in participant_dict.keys():
            participant_dict[person] += 1
        else:
            participant_dict[person] = 1

    for remove in completion:
        participant_dict[remove] -= 1

    return ''.join([x for x, y in participant_dict.items() if y != 0])
