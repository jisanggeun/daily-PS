# 백준: 제곱수 찾기
# https://www.acmicpc.net/problem/1025

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
answer = -1

for i in range(n):
    arr.append(list(map(int, input().strip())))

for i in range(n):
    for j in range(m):
        for di in range(-(n - 1), n):
            for dj in range(-(m - 1), m):
                if di == 0 and dj == 0:
                    num = arr[i][j]
                    if int(num ** 0.5) ** 2 == num:
                        answer = max(answer, num)
                    continue
                num = 0
                r, c = i, j

                while 0 <= r < n and 0 <= c < m:
                    num = num * 10 + arr[r][c]

                    if int(num ** 0.5) ** 2 == num:
                        answer = max(answer, num)

                    r += di
                    c += dj
print(answer)

    # 방식
    # 1. 표의 각 칸을 한 글자씩 숫자로 저장
    # 2. 4중 for문으로 모든 시작점(i, j)과 모든 공차(di, dj) 조합 완전 탐색
        # 2-1. 공차 둘 다 0이면 해당 칸 숫자 하나만 완전제곱수 체크 진행
        # 2-2. 공차가 있으면 범위 안에서 공차만큼 반복 이동하며 숫자 이어붙이기 진행
    # 3. 이어붙인 숫자가 완전제곱수일 경우 answer 업데이트
    # 4. 완전제곱수를 못 찾을 경우 -1 출력