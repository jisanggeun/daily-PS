# 백준: 고층 건물
# https://www.acmicpc.net/problem/1027

import sys
input = sys.stdin.readline

n = int(input().strip())
height = list(map(int, input().split()))

cnt = []

for i in range(n):
    cur_cnt = 0
    
    min_slope = float("inf")
    max_slope = float("-inf")

    # left
    for j in range(i - 1, -1, -1):
        slope = (height[j] - height[i]) / (j - i) 
        if slope < min_slope:
            cur_cnt += 1
            min_slope = slope

    # right
    for j in range(i + 1, n):
        slope = (height[j] - height[i]) / (j - i)
        if slope > max_slope:
            cur_cnt += 1
            max_slope = slope
    cnt.append(cur_cnt)

print(max(cnt))

    # 방식
    # 1. 각 건물(i) 기준으로 왼쪽, 오른쪽 각각 기울기 비교 진행
        # 1-1. 왼쪽의 경우, i-1 ~ 0까지 기울기가 점점 작아져야 보임 (min_slope 업데이트 진행)
        # 1-2. 오른쪽의 경우, i+1 ~ n-1까지 기울기가 점점 커져야 보임 (max_slope 업데이트 진행)
    # 2. 각 건물에서 보이는 건물 수를 cnt에 저장
    # 3. max(cnt)가 정답이므로 출력