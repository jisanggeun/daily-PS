# 백준: A와 B 2
# https://www.acmicpc.net/problem/12919

import sys

input = sys.stdin.readline

s = input().strip()
t = input().strip()

def dfs(t):
    if len(t) == len(s):
        if t == s:
            print("1")
            exit()
        return

    if t[-1] == "A":
        dfs(t[:-1])

    if t[0] == "B":
        dfs(t[::-1][:-1])

dfs(t)   
print(0)

    # 방식
    # 1. 역추적 DFS 사용
    # 2. T에서 S로 역방향으로 줄여나감
        # 2-1. T의 마지막 글자가 A라면, 마지막 글자 A 제거 후 DFS
        # 2-2. T의 첫 글자가 B라면, reverse 후 마지막 글자 B 제거
        # 2-3. 두 조건이 동시에 해당 될 수 있으므로, 둘 다 if문 사용 (둘 다 탐색)
    # 3. len(t) == len(s)일 때, t == s면 문자를 찾은 것이므로 1 출력 후 exit()으로 종료
    # 4. 모든 탐색 실패 시 0 출력