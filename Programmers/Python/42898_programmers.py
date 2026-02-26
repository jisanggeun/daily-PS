# 프로그래머스: 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    answer = 0
    
    dp = [[0] * m for i in range(n)]
    maps = [[0] * m for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            maps[i][j] = 1
            
    for i in range(len(puddles)):
        maps[puddles[i][1] - 1][puddles[i][0] - 1] = 0
        
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif maps[i][j] == 0:
                dp[i][j] = 0
                continue
            elif i > 0 and j > 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]
    
    answer = dp[n-1][m-1] 
    
    return answer % 1000000007

    # 방식
    # 1. maps 배열(지도)에 웅덩이 = 0, 길 = 1로 생성
    # 2. dp[0][0] = 1(시작점)부터 이중 for문 사용해 Bottom-Up DP 사용
        # 2-1. 만약 웅덩이일 시, 0 set (if maps[i][j] == 0)
        # 2-2. 웅덩이가 아닐 시, 위쪽 + 왼쪽 경로 수 누적 합 (dp[i-1][j] + dp[i][j-1])
    # 3. 경로 수를 1,000,000,007로 나눈 나머지를 return 하라는 조건이 있었으므로 % 써서 return