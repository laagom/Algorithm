def solution(d, budget):
    budget_limit = 0
    dept = []
    
    d = sorted(d)
    for num in d:
        budget_limit += num
        dept.append(num)
        if budget_limit > budget:
            budget_limit -= num
            dept.pop()
            
        print(f'd: {num}')
        print(f'budget_limit: {budget_limit}')
        print(f'dept: {dept}')
        
        
    return len(dept)