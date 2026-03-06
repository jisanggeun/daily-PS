# 백준: 입국심사
# https://www.acmicpc.net/problem/3079

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
answer = 0

for i in range(n):
    arr.append(int(input().strip()))

max_time = max(arr)
low, high = 1, max_time * m # 최악 == high --> 심사 대상 인원 m * 최대 걸리는 시간 max_time

while low <= high:
    mid = (low + high) // 2

    total = sum(mid // t for t in arr)
    if total >= m:
        answer = mid
        high = mid - 1 
    else:
        low = mid + 1

print(answer)
    
    # 방식
    # 1. 이분 탐색으로 시간의 최솟값 탐색
    # 2. low = 1, high = 가장 느린 심사관이 혼자 m명 처리하는 시간
    # 3. mid분 동안 각 심사관이 처리 가능한 인원 (mid // t) total로 합산
        # 3-1. total >= m인 경우, answer = mid로 하고 시간 줄이기 (high = mid - 1)
        # 3-2. 아닌 경우, low = mid + 1로 늘려 탐색 