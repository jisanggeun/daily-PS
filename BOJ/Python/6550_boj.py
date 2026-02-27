# 백준: 부분 문자열
# https://www.acmicpc.net/problem/6550

import sys

for line in sys.stdin:
    s, t = line.split()

    idx = 0

    for j in range(len(t)):
        if(t[j] == s[idx]):
            idx += 1
            if idx == len(s):
                break

    if idx == len(s):
        print("Yes")
    else: 
        print("No")

    # 방식
    # 1. s가 t의 subsequence(부분 수열)인지 판별하는 문제
    # 2. idx로 s에서 현재 찾을 문자 위치를 추적
    # 3. t를 앞에서부터 순회하며 s[idx]와 일치하면 idx += 1
        # 3-1. idx == len(s)이면 s의 모든 문자를 순서대로 찾은 것 → "Yes"
        # 3-2. t를 끝까지 돌아도 idx < len(s)이면 → "No"
    # 4. 입력은 EOF까지 반복됨
