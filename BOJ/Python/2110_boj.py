# 백준: 공유기 설치
# https://www.acmicpc.net/problem/2110

import sys

input = sys.stdin.readline

n, c = map(int, input().split())
location = []

for i in range(n):
    location.append(int(input().strip()))

location.sort()

low, high = 1, location[-1] - location[0]

while low <= high:
    mid = (low + high) // 2 # 거리

    # check
    idx, router_cnt = 0, 1
    for i in range(1, n):
        if location[idx] + mid <= location[i]:
            idx = i 
            router_cnt += 1
        
    if router_cnt >= c:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)

    # 방식
    # 1. 이분 탐색으로 공유기 간 최소거리의 최댓값 구함
    # 2. 처음 low = 1, high = 최악이므로, 가장 먼 두 집 사이 거리 (location[-1] - location[0]) 
    # 3. 처음 집에 공유기를 설치해야하므로, router_cnt = 1
    # 4. 이전 공유기 설치 위치에서 mid 거리 이상 떨어진 집이 나와야 다음 공유기 설치하고 개수 카운트 + 1
        # 3-1. router_cnt >= c인 경우, c보다 많이 설치 됐으므로, 거리를 늘려야 함 --> answer = mid, low = mid + 1
        # 3-2. router_cnt < c인 경우, c보다 적게 설치 됐으므로, 거리를 줄여야 함 --> high = mid -1 