# 백준: 휴게소 세우기
# https://www.acmicpc.net/problem/1477

import sys

input = sys.stdin.readline

n, m, l = map(int, input().split())

location = list(map(int, input().split()))
location.append(0)
location.append(l)
location.sort()
diff_loc = []

answer = 0
low, high = 1, location[-1] - location[0]

for i in range(1, len(location)):
    diff_loc.append(location[i] - location[i - 1])

while low <= high:
    mid = (low + high) // 2
    
    # 각 구간을 mid 이하로 나누는 데 필요한 휴게소 수 계산
    cnt = 0
    for diff in diff_loc:
        cnt += (diff - 1) // mid
    
    # check (최댓값의 최솟값이므로, 가능하면 mid 줄이기)
    if cnt <= m:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

print(answer)
    
    # 방식
    # 1. 휴게소 위치에 0과 l 추가 후 정렬, 인접 구간 차이(diff_loc) 계산
    # 2. 이분 탐색으로 구간 최댓값(mid) 탐색
        # 2-1. 각 구간을 mid 이하로 나누는 데 필요한 휴게소 수 계산 (diff - 1) // mid
        # 2-2. 필요한 수 <= m: 이면 가능 --> mid 줄이기 (answer = mid, high = mid - 1)
        # 2-3. 필요한 수 > m: 이면 불가능 --> mid 늘리기 (low = mid + 1)
    # 3. 최댓값의 최솟값이므로 가능하면 mid를 줄임