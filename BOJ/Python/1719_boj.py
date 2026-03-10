# 백준: 택배
# https://www.acmicpc.net/problem/1719

import sys
input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
dist = [[INF] * (n + 1) for i in range(n + 1)]
des_dist = [[0] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for i in range(m):
    a, b, w = map(int, input().split())
    dist[a][b] = w
    dist[b][a] = w

    des_dist[a][b] = b
    des_dist[b][a] = a

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                des_dist[i][j] = des_dist[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print('-', end = ' ')
        else: 
            print(des_dist[i][j], end = ' ')
    print()

    # 방식
    # 1. dist를 INF로, des_dist를 0으로 초기화 진행 (자기 자신 dist[i][i] = 0)
    # 2. 간선 입력 시 dist에 가중치, des_dist에 직접 연결된 다음 노드 저장
    # 3. 플로이드-워셜로 최단거리 갱신 시, des_dist[i][j] = des_dist[i][k] (i -> j 경로의 첫 노드)
    # 4. des_dist[i][j]로 i에서 j로 갈 때 다음에 방문할 노드 출력