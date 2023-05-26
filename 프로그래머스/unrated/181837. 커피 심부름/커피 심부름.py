def solution(order):
    amount  = 0
    coffees = {'americano': 4500 , 'cafelatte': 5000, 'anything': 4500} 

    for coffee in order:
        if 'americano' in coffee:
            amount += coffees['americano']
        elif 'cafelatte' in coffee:
            amount += coffees['cafelatte']
        elif 'anything' in coffee:
            amount += coffees['anything']

    return amount