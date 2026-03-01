# 백준: 회문
# https://www.acmicpc.net/problem/17609

def pseudo_check(current_idx, left, right):
    while left < right:
        if str_arr[current_idx][0][left] != str_arr[current_idx][0][right]:
            return False
        left += 1
        right -= 1
    return True

import sys

input = sys.stdin.readline

t = int(input())
str_arr = []

for i in range(t):
    str_arr.append([input().strip(), 0])


for i in range(len(str_arr)):
    for j in range(len(str_arr[i][0]) // 2):
        if str_arr[i][0][j] != str_arr[i][0][len(str_arr[i][0]) - 1 - j]: 
            if pseudo_check(i, j + 1, len(str_arr[i][0]) - 1 - j) or pseudo_check(i, j, len(str_arr[i][0]) - 2 - j):
                str_arr[i][1] = 1
            else:
                str_arr[i][1] = 2
            break

for i in range(t):
    print(str_arr[i][1])

    # 방식
    # 1. 회문 판단 ( // 2 사용 시 length가 홀수든 짝수든 계산할 필요 없음)    
    # 2. 만약 회문 판단 시 글자가 다를 경우
        # 2-1. j + 1 ~ len(str_arr[i][0]) - 1 - j 까지 회문 돌려보고 결과 T/F로 
        # 2-2. j ~ len(str_arr[i][0]) - 2 - j 까지 회문 돌려보고 결과 T/F로
    # 3. 2-1 결과와 2-2 결과 OR문으로
        # 3-1. true 나올 시 str_arr[i][1] = 1 
        # 3-2. false 나올 시 str_arr[i][1] = 2
    # 4. 그 이후 break 진행