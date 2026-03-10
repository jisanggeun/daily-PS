# 백준: 서강그라운드
# https://www.acmicpc.net/problem/14938

import sys
input = sys.stdin.readline
INF = float('inf')

n, m, r = map(int, input().split())

dist = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(n + 1):
    dist[i][i] = 0

lists = list(map(int, input().split()))

max_item = 0

for i in range(r):
    a, b, w = map(int, input().split())
    dist[a][b] = min(dist[a][b], w)
    dist[b][a] = min(dist[b][a], w)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n + 1):
    ans = lists[i - 1]
    for j in range(1, n + 1):
        if i == j: 
            continue
        elif dist[i][j] <= m:
            # 계산
            ans += lists[j - 1]
    max_item = max(max_item, ans)

print(max_item)

    # 방식
    # 1. dist 2차원 배열을 INF로 초기화 후, 자기 자신([i][i])은 0으로 set
    # 2. 간선 입력받고, dist[a][b], dist[b][a]에 가중치 저장 (양방향, 중복 간선의 경우 min)
    # 3. 플로이드-워셜로 모든 노드 간 최단거리 계산
    # 4. 각 노드에서 수색범위(m) 이내인 노드들의 아이템 합산
    # 5. 합산 최댓값이 answer