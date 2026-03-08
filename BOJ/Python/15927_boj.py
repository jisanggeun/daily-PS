# 백준: 회문은 회문아니야!!
# https://www.acmicpc.net/problem/15927

import sys
input = sys.stdin.readline

str_arr = list(input().strip())
n = 2

#print(str_arr, str_arr[-3])

for i in range(len(str_arr) // 2):
    if str_arr[i] != str_arr[-(1 + i)]:
        n = 0
        break

if n == 0:
    print(len(str_arr))
else:
    for i in range(1, len(str_arr) // 2 + 1):
        if str_arr[i - 1] != str_arr[i]:
            n = 1
            break

    if n == 1:
        print(len(str_arr) - 1)
    elif n == 2:
        print(-1)
    
    # 방식
    # 1. 입력 문자열이 회문인지 확인 (양 끝부터 비교)
    # 2. 회문이 아니면, 전체 길이가 answer
    # 3. 회문이면, 이미 앞에서 회문인걸 확인했기 때문에
        # 3-1. 양 옆이 다른 문자일 시, 전체 길이에서 -1 할 시, answer
        # 3-2. 다 같은 문자로 이루어진 문자열일 시, -1이 answer