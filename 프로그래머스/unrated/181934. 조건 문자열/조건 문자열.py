def solution(ineq, eq, n, m):
    eq = ""
    eq = eq if eq == "=" else ""

    if eval(str(n)+ineq+eq+str(m)):
        return 1
    else:
        return 0