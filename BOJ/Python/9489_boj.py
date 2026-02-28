# 백준: 사촌
# https://www.acmicpc.net/problem/9489

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

while n != 0 and k != 0:
    test = list(map(int, input().split()))

    result = []
    conti = [test[0]]
    tree = {}
    q = deque()

    k_parent_sibling = []
    answer = 0

    # 연속된 수 그룹화
    for i in range(1, n):
        if test[i - 1] + 1 == test[i]:
            conti.append(test[i])
        else:
            result.append(conti)
            conti = [test[i]]
    result.append(conti)

    # 트리 만들기        
    root = result[0][0]
    tree[root] = []
    q.append(root)

    for i in range(1, len(result)):
        parent = q.popleft()
        tree[parent] = result[i]
        for c in result[i]:
            tree[c] = []
            q.append(c)

    # i = k의 부모 노드
    for i in tree:
        if k in tree[i]:
            k_parent = i

    # i의 부모에서 자식노드 뽑아서 i 제외
    for i in tree:
        if k_parent in tree[i]:
            k_parent_sibling = [c for c in tree[i] if c!= k_parent]

    for i in k_parent_sibling:
        for j in range(len(tree[i])):
            answer += 1
        
    print(answer)
    n, k = map(int, input().split())

    # 방식
    # 1. 연속된 수끼리 그룹으로 묶음
    # 2. 큐로 트리 구현
        # 2-1. 첫번째 그룹에서 루트 노드 꺼내 트리에 등록 후 큐에 넣음
        # 2-2. 큐 앞에서 노드를 꺼낼 시 그 노드가 부모가 되고 바로 다음 그룹 전체가 해당 부모노드의 자식이 됨 
        # 2-3. 자식 노드들도 마찬가지로, 큐에 넣고, 자기 차례가 올 시 부모 노드가 됨
        # 2-4. (큐의 FIFO로 자식이 없는 노드 중 가장 작은 노드에 자동으로 배정)
    # 3. K의 부모 노드 찾기
    # 4. K 부모의 부모의 자식 노드 뽑고, K 부모 제외
    # 5. K 부모의 sibling 노드 중 자식노드 개수 합산 