# 백준: 부분 삼각 수열
# https://www.acmicpc.net/problem/1548

import sys

input = sys.stdin.readline

n = int(input().strip())

max_length = min(n, 2)

arr = list(map(int, input().split()))

sort_arr = sorted(arr)

for j in range(len(sort_arr) - 1, -1, -1):
    for i in range(1, j):
        if sort_arr[i - 1] + sort_arr[i] > sort_arr[j]:
            length = j - i + 2
            max_length = max(max_length, length)
            break

print(max_length)

    # 방식
    # 1. 배열 오름차순으로 정렬
    # 2. 정렬 후 연속 구간에서, 가장 작은 두 수의 합 (i - 1 + i 번째) > 가장 큰 수(j)면 삼각 수열
        # 2-1. sort_arr[i-1] + sort_arr[i] > sort_arr[j]시, 만족하는 삼각 수열 길이 = j - (i - 1) + 1
        # 2-2. 조건 만족하면 break (더 이상 만족해도 max_length 업데이트 불가)
    # 3. max_length 초기 값 = min(n, 2) 
        # 3-1. n이 2개 이하면 삼각 수열 조건 검사할 필요가 없음