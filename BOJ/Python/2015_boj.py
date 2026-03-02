# 백준: 수들의 합 4
# https://www.acmicpc.net/problem/2015

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

answer = 0

arr = list(map(int, input().split()))

sum_arr = [0]
sum_cnt = {}

for i in range(n):
    sum_arr.append(sum_arr[i] + arr[i]) 

# 지금 보는 값 - k = 이전에 있었던 값
for i in range(len(sum_arr)):
    
    # 지금 보는 값 - k가 dict 안에 있는지 확인
    if sum_arr[i] - k in sum_cnt:
        # 있으면, cnt만큼 answer ++
        answer += sum_cnt[sum_arr[i] - k]

    # 지금 값 dict에 넣음 (이미 있었으면, cnt + 1, 없으면 1)
    sum_cnt[sum_arr[i]] = sum_cnt.get(sum_arr[i], 0) + 1

print(answer)

    # 방식
    # 1. 누적합 배열 (sum_arr) 생성 
        # 1-1. sum_arr[j + 1] - sum_arr[i] = arr[i] ~ arr[j] 구간 합 의미
    # 2. dict로 이전에 나온 누적합 값의 등장 횟수(sum_cnt) 저장
    # 3. sum_arr 순회하며, 지금 값 - k가 dict 안에 있는지 확인
        # 3-1. 만약 있으면, 등장 횟수만큼 answer ++ (합이 k인 구간이 cnt만큼 존재함 의미)
        # 3-2. 지금 값을 dict에 저장 (이미 있으면 cnt + 1, 없으면 1)
    # 4. 확인하고 저장 하는 순서가 중요함 (j == i인 경우까지 셀 수 있기 때문)

#[0, [0], [0,1], [0,1,2], [0,1,2,3]]