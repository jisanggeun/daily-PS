# 백준: 명제 증명
# https://www.acmicpc.net/problem/2224

import sys

input = sys.stdin.readline

n = int(input().strip())

propose_set = set()

for i in range(n):
    first, sign, second = input().split()
    if first == second:
        continue
    propose_set.add((first, second))

while True:
    propose_list = list(propose_set)
    prev_set_len = len(propose_set)

    for i in range(len(propose_list)):
        for j in range(len(propose_list)):
            if i == j:
                continue
            elif propose_list[i][0] == propose_list[j][1]:
                if propose_list[j][0] != propose_list[i][1]:
                    propose_set.add((propose_list[j][0], propose_list[i][1]))
    
    if len(propose_set) == prev_set_len:
        break

sorted_list = sorted(propose_set)

print(len(sorted_list))
for i in range(len(sorted_list)):
    print(sorted_list[i][0], sign, sorted_list[i][1])

    # 방식
    # 1. 입력받은 명제를 first, sign, second로 split해 입력 받아 tuple로 저장
        # 1-1. 만약 first == second이면, 제외
    # 2. 새로운 명제가 안생길 때 까지 while문 반복
        # 2-1. 모든 명제의 pair을 비교해, i의 first == j의 second면 삼단 논법 적용
        # 2-2. j의 first와 i의 second를 비교해 다를 경우만 (j의 first, i의 second)를 새로운 명제로 set에 추가
        # 2-3. 같은 경우 (A => A)와 같이 first == second이므로, 제외
        # 2-4. set 크기가 변하지 않으면 while문 종료
    # 3. 정렬 후 출력 