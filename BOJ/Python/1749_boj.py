# 백준: 점수따먹기
# https://www.acmicpc.net/problem/1749

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
cum_arr = [[0] for i in range(n)]

answer = float('-inf') # 모든 배열 음수 대비

# 배열 저장
for i in range(n):
    arr.append(list(map(int, input().split())))

# cummulative 배열 저장
for i in range(n):
    for j in range(m):
        cum_arr[i].append(cum_arr[i][j] + arr[i][j])

for start in range(n):
    temp_arr = [0] * (m + 1)
    for end in range(start, n):
        for j in range(1, m + 1):
            temp_arr[j] += cum_arr[end][j]

        min_v = temp_arr[0]
        best = temp_arr[1] - temp_arr[0]

        for j in range(1, m + 1):
            best = max(best, temp_arr[j] - min_v)
            min_v = min(min_v, temp_arr[j]) 

        answer = max(answer, best)

print(answer)

    # 방식
    # 1. 가로 누적합(cum_arr) 생성
    # 2. 세로 범위(start ~ end)를 이중 for문으로 모든 경우 탐색 진행
    # 3. 세로 범위 내 가로 누적합을 temp_arr에 누적
    # 4. temp_arr에서 min_v(최소 누적값) 추적하며, 최대 구간합(best) 계산
        # 4-1. 구간합 = temp_arr[j] - min_v (빼는 값이 작을수록 결과는 커짐)
    # 5. 모든 경우 탐색 후 best가 answer