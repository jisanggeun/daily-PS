# 백준: 호석이 두 마리 치킨
# https://www.acmicpc.net/problem/21278

import sys
input = sys.stdin.readline

INF = float("inf")

n, m = map(int, input().split())
dist = [[INF] * (n + 1) for i in range(n + 1)]

loc = [0, 0]
cost = 0

for i in range(1, n + 1):
    dist[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())

    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        total = 0

        for k in range(1, n + 1):
            total += min(dist[k][i], dist[k][j]) * 2

        if cost == 0:
            loc = [i, j]
            cost = total
        else:
            if cost > total:
                cost = total
                loc = [i, j]
            elif cost == total:
                if loc[0] > i:
                    loc[0] = i
                    loc[1] = j
                elif loc[0] == i and loc[1] > j:
                    loc[1] = j
                    
print(loc[0], loc[1], cost)

    # 방식
    # 1. dist를 INF로 초기화하고, 자기 자신[i][i] = 0, weight의 경우 모두 1로 저장
    # 2. 플로이드-워셜 방식 사용해 모든 노드 간 최단 거리 계산 
    # 3. 치킨집 2개 조합(combination)을 이중 for문 사용해 완전 탐색 진행 (i < j)
    # 4. 각 조합마다 모든 건물(k)에서 가까운 치킨집까지 왕복거리 계산 (*2 하면 됨)
    # 5. 계산값 최소인 조합을 저장하고, 동일하면 건물 번호가 작은 조합을 우선적으로 저장하게끔 하고 출력