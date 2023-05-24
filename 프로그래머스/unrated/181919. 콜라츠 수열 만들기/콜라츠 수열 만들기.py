class Calc:
    answer = []
    
    def getList(self):
        return self.answer
    
    def calc_(self, n):
        self.answer.append(n)
        if n%2 == 0:
            n = n/2
        else:
            n = (3*n) + 1
        return int(n)

    
def solution(n):
    answer = []
    calc = Calc()
    while n > 1:
        n = calc.calc_(n)
    calc.answer.append(1)        
    return calc.getList()