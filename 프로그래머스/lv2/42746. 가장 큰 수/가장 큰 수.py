def solution(numbers):
    
    # numbers요소를 문자열로 변환
    arry = list(map(str, numbers))

    # lambda 함수로 str으로 변환된 요소를 3번씩 이어붙인 값을 역정렬
    arry.sort(key=lambda x: x*3, reverse=True)
        
    # 0, 0, 0 인 경우 테스트 케이스 통과하지 못하는 경우 발생 int형으로 변경우 str으로 재 변경
    return str(int(''.join(arry)))