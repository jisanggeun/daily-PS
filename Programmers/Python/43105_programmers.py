# 프로그래머스: 정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    answer = 0

    for i in range(len(triangle) - 1, 0, -1):
        for j in range(len(triangle[i]) - 1):
            k = j + 1
            val = max(triangle[i][j], triangle[i][k])
            triangle[i - 1][j] = triangle[i - 1][j] + val

    answer = triangle[0][0]

    return answer

    # 방식
    # 1. 삼각형 맨 아래 줄부터 위로 올라가는 Bottom-Up DP로 해결
    # 2. 인접한 두 child 중 max 값 골라 바로 윗줄에 누적으로 합침
    # 3. 맨 꼭대기 triangle(triangle[0][0])에 최대 경로 합이 남게 됨