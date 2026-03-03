# 백준: 나머지 합
# https://www.acmicpc.net/problem/10986

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
cum_arr = [0]
cum_cnt = {}

answer = 0

# 누적 합 
for i in range(n):
    cum_arr.append(cum_arr[i] + arr[i])

# 나머지 등장 횟수 세서 dict에 저장
for i in range(len(cum_arr)):
    # 나머지
    r = cum_arr[i] % m
    
    # 이전에 같은 나머지 나온 적 있으면, 횟수만큼 answer++
    # (나머지가 같은 두 누적합 차이는 m으로 나눠 떨어짐)
    # (cum_arr[j] - cum_arr[i]) % m == 0 -> cum_arr[j] % m == cum_arr[i] % m
    if r in cum_cnt:
        answer += cum_cnt[r]
    # 현재 나머지를 dict에 저장 (이미 있으면 cnt + 1, 없으면 1)
    cum_cnt[r] = cum_cnt.get(r, 0) + 1

print(answer)

    # 방식
    # 1. 누적합 배열 (cum_arr) 선언
    # 2. cum_arr의 각 값을 m으로 나눈 나머지의 등장 횟수를 dict에 저장
    # 3. 이전에 같은 나머지가 나온적 있으면, 횟수만큼 answer++
        # 3-1. 나머지가 같은 쌍끼리 빼면 m으로 나눠 떨어짐 
    # 4. 현재 나머지 dict에 저장 (이미 있으면 cnt + 1, 없으면 1)
    # 5. 확인하고 저장하는 순서 중요함 (j == i인 경우까지 셀 수 있기 때문)