# 백준: 문자열 게임 2
# https://www.acmicpc.net/problem/20437

import sys

input = sys.stdin.readline

t = int(input().strip())

for loop_idx in range(t):

    char_pos = {}
    min_length = 10001
    max_length = 0

    #print(t)

    w = input().strip()
    k = int(input().strip())

    #print(w, k)

    # 문자열 position 저장
    for i in range(len(w)):
        if w[i] not in char_pos:
            char_pos[w[i]] = []
        char_pos[w[i]].append(i)

    #print(char_pos)

    for char in char_pos:
        #print(char_pos[char])
        for i in range(len(char_pos[char]) - k + 1):
            #print(char, char_pos[char][i], char_pos[char][i + k - 1])
            length = char_pos[char][i + k - 1] - char_pos[char][i] + 1
            min_length = min(min_length, length)
            max_length = max(max_length, length)

    if min_length == 10001 or max_length == 0:
        print("-1")
    else:
        print(min_length, max_length)

    # 방식
    # 1. 맨 처음 문자열 순회하면서 각 문자별 등장 index를 dict(char_pos)에 저장
    # 2. 각 문자의 위치 list에서 k개 간격(문제 조건) 으로 sliding
        # 2-1. i+k-1번째 - i번째 + 1 == 해당 구간의 문자열 길이를 의미
        # 2-2. k개 포함하는 가장 짧은 문자열 == 첫 번째와 마지막 글자가 해당 문자로 같을 수 밖에 없음
    # 3. sliding 하며 min_length, max_length 업데이트
    # 4. 만족하는 문자열 없을 시 -1 출력
