# 백준: 트리의 기둥과 가지
# https://www.acmicpc.net/problem/20924

import sys
from collections import deque

input = sys.stdin.readline

n, r = map(int, input().split())

tree = {}
q = deque()
max_len, pillar_num, pillar_cost = 0, 0, 0

visit = set()

for i in range(1, n + 1):
    tree[i] = []

for i in range(n - 1):
    parent, child, cost = map(int, input().split())

    tree[parent].append((child, cost))
    tree[child].append((parent, cost))

visit.add(r)

children_cnt = 0

for i in range(len(tree[r])):
    if tree[r][i][0] not in visit:
        children_cnt += 1

if children_cnt >= 2 and pillar_num == 0:
    pillar_num = r
    pillar_cost = 0

for i in range(len(tree[r])):
    if tree[r][i][0] not in visit:
        visit.add(tree[r][i][0])
        q.append((tree[r][i][0], tree[r][i][1]))

while len(q) != 0:
    next = q.popleft()
    max_len = max(max_len, next[1])

    children_cnt = 0

    for i in range(len(tree[next[0]])):
        if tree[next[0]][i][0] not in visit:
            children_cnt += 1

    if children_cnt >= 2 and pillar_num == 0:
        pillar_num = next[0]
        pillar_cost = next[1]

    for i in range(len(tree[next[0]])):
        if tree[next[0]][i][0] not in visit:
            visit.add(tree[next[0]][i][0])
            q.append((tree[next[0]][i][0], next[1] + tree[next[0]][i][1]))

if pillar_num == 0:
    pillar_cost = max_len

print(pillar_cost, max_len - pillar_cost)

    # 방식
    # 1. 양방향 인접 리스트로 트리 구현
    # 2. BFS로 루트부터 탐색하며 visit으로 방문 체크
    # 3. 각 노드에서 visit 안 한 이웃 노드 수(children_cnt) 세서 분기 판단
        # 3-1. children_cnt >= 2일 시, 분기 --> 기둥 끝 (pillar_num, pillar_cost 저장)
        # 3-2. children_cnt < 2일 시, 일직선이므로, 기둥 계속 이어짐
    # 4. BFS 돌면서 max_len에 루트부터 각 노드까지 최대 거리 저장
    # 5. 분기 없으면, (pillar_num == 0) 전체가 기둥 --> pillar_cost = max_len
    # 6. 기둥 길이, 가지 길이(max_len - pillar_cost) 출력 