# 백준: 트리의 순회
# https://www.acmicpc.net/problem/2263

import sys

input = sys.stdin.readline
sys.setrecursionlimit(200000)

def recursive(in_start, in_end, post_start, post_end):
    # 구간 없으면 종료
    if in_start > in_end:
        return
        
    # 후위 순회 마지막 값 = 현재 구간 root
    root = post_arr[post_end]
    # 중위 순회에서 root 위치
    root_idx = pos[root]

    # 왼쪽 sub tree 크기
    left_size = root_idx - in_start

    # root 출력 -> 왼쪽 재귀 -> 오른쪽 재귀
    print(root, end=" ")

    recursive(in_start, root_idx - 1, post_start, post_start + left_size - 1)
    recursive(root_idx + 1, in_end, post_start + left_size, post_end - 1)    

n = int(input().strip())

in_arr = list(map(int, input().split())) # left -> root -> right
post_arr = list(map(int, input().split())) # left -> right -> root

# root -> left -> right
pos = {}

# index
for i in range(n):
    pos[in_arr[i]] = i 

recursive(0, n - 1, 0, n - 1)

    # 방식
    # 1. 후위 순회(post_order)의 마지막 값 = 해당 구간의 root 의미
    # 2. 중위 순회(in_order)에서 root 위치 찾고 left sub-tree 크기(left_size) 계산
    # 3. root 출력 -> 왼쪽 재귀 -> 오른쪽 재귀 순으로 진행
    # 4. 중위/후위의 시작 - 끝 index가 다를 수 있으므로, 4개 인자(in_start, in_end, post_start, post_end)로 구간 추적