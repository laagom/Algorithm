def solution(myStr):
    temp = myStr.replace('c', 'a').replace('b','a').split('a')
    answer = [string for string in temp if string != ""]
    return answer if answer else ["EMPTY"]