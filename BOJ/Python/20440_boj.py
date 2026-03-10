# 백준: 니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마
# https://www.acmicpc.net/problem/20440

import sys
input = sys.stdin.readline

n = int(input().strip())

d = {}

for i in range(n):
    s, e = map(int, input().split())
    d[s] = d.get(s, 0) + 1
    d[e] = d.get(e, 0) - 1

# dict의 (key, value) pair 전부 정렬
mos_time = sorted(d.items())

cum_cnt = 0
max_cnt = 0
max_time_s = 0
max_time_e = 0

for time, cnt in mos_time:
    cum_cnt += cnt 

    if cum_cnt > max_cnt:
        max_cnt = cum_cnt
        max_time_s = time
        max_time_e = 0
    
    if max_cnt > cum_cnt and max_time_e == 0:
        max_time_e = time

print(max_cnt)
print(max_time_s, max_time_e)

    # 방식
    # 1. dict로 start time에 모기 +1, end time에 모기 -1 기록
    # 2. d.items()로 (시간, 합산된 cnt) 쌍 꺼내 시간순으로 정렬
    # 3. 누적합(cum_cnt)로 스위핑
        # 3-1. cum_cnt > max_cnt면 새 최대 구간 시작(start time 업데이트, end time 리셋)
        # 3-2. cum_cnt < max_cnt고, end가 없으면 그 시점이 구간의 끝임
    # 4. 최대 모기 수(max_cnt)와 최대 구간(max_time_s, max_time_e) 출력