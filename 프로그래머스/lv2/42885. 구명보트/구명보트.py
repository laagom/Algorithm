from collections import deque
def solution(people, limit):
    people = deque(sorted(people))
    count = 0
    
    while people:
        if len(people) == 1:
            count += 1
            break

        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()      
        else:
            people.pop()
        count += 1
    return count