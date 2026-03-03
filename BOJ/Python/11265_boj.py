# 백준: 끝나지 않는 파티
# https://www.acmicpc.net/problem/11265

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cost = []
req = []

for i in range(n):
    cost.append(list(map(int, input().split())))

# floyd
for k in range(n):
    for i in range(n):
        for j in range(n):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

for i in range(m):
    req.append(list(map(int, input().split())))

for i in range(m):
    cur = req[i][0]
    des = req[i][1]
    time = req[i][2]

    if cost[cur - 1][des - 1] <= time:
        print("Enjoy other party")
    else:
        print("Stay here")

    # 방식
    # 1. n * n cost 배열 입력 받음
    # 2. 플로이드 워셜 방식으로 모든 pair에 대해 최단 거리 저장
        # 2-1. 모든 노드 k를 경유지로 시도
        # 2-2. cost[i][k] + cost[k][j] < cost[i][j]면, cost[i][j] = cost[i][k] + cost[k][j]로 업데이트
    # 3. 각 request마다 cost[i][j] <= time이면, Enjoy other party 출력, 아니면 Stay here 출력