def solution(my_string, queries):
    answer = ''

    for query in queries:
        s, e = query
        my_string = my_string[:s] + my_string[e: None if s-1 < 0 else s-1:-1] + my_string[e+1:]  
    return my_string

