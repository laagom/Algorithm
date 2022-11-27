from collections import deque
def solution(spell, dic):
    answer = 0

    for word in dic:
        deque_spell = deque(spell)
        
        for char in deque(spell):
            if char in list(word):
                print(char)
                deque_spell.popleft()

        answer += 1 if not deque_spell else 0

    if answer > 0:
        return 1
    else:
        return 2