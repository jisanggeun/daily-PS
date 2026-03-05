# 백준: 학부 연구생 민상
# https://www.acmicpc.net/problem/21922

import sys
from collections import deque 

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
visit = [[[False] * 4 for i in range(m)] for j in range(n)] # visit[y][x][direction]

q = deque()

for j in range(n):
    arr.append(list(map(int, input().split())))

# 상하 좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0
 
for j in range(n):
    for i in range(m):
        if arr[j][i] == 9:
            # 에어컨 위치는 이미 방문한 거이므로, true로 set
            visit[j][i] = [True, True, True, True]
            for d in range(4):
                cur_j, cur_i, cur_d = j, i, d 

                while True:
                    # next location
                    next_j = cur_j + dy[cur_d]
                    next_i = cur_i + dx[cur_d]

                    # 범위 밖 검사
                    if not (0 <= next_j < n and 0 <= next_i < m):
                        break
                    # 다음 arr에서 통과 혹은 반사되는 direction 설정
                    if arr[next_j][next_i] == 9:
                        break
                    elif arr[next_j][next_i] == 1:
                        if cur_d == 0 or cur_d == 1:
                            cur_d = cur_d
                        elif cur_d == 2:
                            cur_d = 3
                        elif cur_d == 3:
                            cur_d = 2
                    elif arr[next_j][next_i] == 2:
                        if cur_d == 2 or cur_d == 3:
                            cur_d = cur_d
                        elif cur_d == 0:
                            cur_d = 1
                        elif cur_d == 1:
                            cur_d = 0
                    elif arr[next_j][next_i] == 3:
                        if cur_d == 0:
                            cur_d = 3
                        elif cur_d == 1:
                            cur_d = 2
                        elif cur_d == 2:
                            cur_d = 1
                        elif cur_d == 3:
                            cur_d = 0
                    elif arr[next_j][next_i] == 4:
                        if cur_d == 0:
                            cur_d = 2
                        elif cur_d == 1:
                            cur_d = 3
                        elif cur_d == 2:
                            cur_d = 0
                        elif cur_d == 3:
                            cur_d = 1
                    else: 
                        cur_d = cur_d
                    
                    # 아직 방문 안했으면 방문
                    if visit[next_j][next_i][cur_d] == True:
                        break
                    visit[next_j][next_i][cur_d] = True
                    cur_j, cur_i = next_j, next_i

for j in range(n):
    for i in range(m):
        if visit[j][i][0] or visit[j][i][1] or visit[j][i][2] or visit[j][i][3]:
            answer += 1

print(answer) 

    # 방식
    # 1. 에어컨(9) 위치에서 4방향으로 while문으로 직진
    # 2. 물건 만나면 cur_d 방향 변경
        # 2-1. 물건 1 -> 상하 통과, 좌우 반사
        # 2-2. 물건 2 -> 좌우 통과, 상하 반사
        # 2-3. 물건 3, 물건 4 -> 방향 전환
    # 3. 에어컨(9) 만나거나, 범위 밖이거나, 이미 방문한 방향이면 break
    # 4. visit[y][x][방향] 3차원 배열로 방문 체크
    # 5. 어떤 방향이든, 하나라도 방문한 칸 수 = answer