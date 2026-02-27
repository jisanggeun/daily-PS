# 백준: 암호 해독
# https://www.acmicpc.net/problem/14584

import sys
input = sys.stdin.readline

encrypt_raw = input()
num = input()

words = [input().strip() for i in range(int(num))]
found = False

encrypt = ''.join(encrypt_raw.split())

for j in range(ord("z") - ord("a") + 1):
    decrypt = []
    # 문자열 복호화
    for i in range(len(encrypt)):
        if ord(encrypt[i]) + j > ord("z"):
            chg = ord(encrypt[i]) + j - ord("z") + ord("a") - 1
        else:
            chg = ord(encrypt[i]) + j   
        
        decrypt.append(chr(chg))

    string = ''.join(decrypt)
    
    # 단어 포함되는지 확인
    for i in range(len(words)):
        string = ''.join(decrypt)
        if words[i] in string:
            print(string)
            found = True
            break
    
    if found == True:
        break

    # 방식
    # 1. 암호문에서 공백 제거
    # 2. a~z shift (0~25)를 모두 시도해 문자열 복호화 진행
        # 2-1. 각 문자에 shift 변수 j를 더함
        # 2-2. ord('z')를 넘으면, ord('a')부터 다시 순환하도록 설정
    # 3. 복호화된 문자열에 주어진 단어가 포함되는지 확인
        # 3-1. 단어가 포함되면 해당 문자열 출력 후 종료