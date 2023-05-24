import datetime

def solution(date1, date2):
    answer = 0

    convert_date1 = datetime.datetime(date1[0], date1[1], date1[2])
    convert_date2 = datetime.datetime(date2[0], date2[1], date2[2])
    
    if convert_date1 < convert_date2:
        return 1
    
    return answer