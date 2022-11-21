def solution(cipher, code):

    return ''.join([char for i, char in enumerate(cipher,1) if i%code == 0])