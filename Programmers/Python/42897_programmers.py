# 프로그래머스: 도둑질
# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    answer = 0
    
    dp_1 = [0] * len(money)
    dp_2 = [0] * len(money)
    
    # 첫번째 집을 터는 경우
    dp_1[0] = money[0]
    dp_1[1] = max(money[0], money[1])
    
    # 첫번째 집을 털었기 때문에, 두번째 집이랑 마지막 집은 못 털음 (원형이기 때문)
    for i in range(2, len(money) - 1):
        dp_1[i] = max(dp_1[i-1], dp_1[i-2] + money[i])   
        
    # 첫번째 집을 안터는 경우
    dp_2[1] = money[1]
    dp_2[2] = max(money[1], money[2])
    
    # 두번째 집은 마지막 집 털 수 있음
    for i in range(3, len(money)):
        dp_2[i] = max(dp_2[i-1], dp_2[i-2] + money[i])
        
    answer = max(dp_1[len(money) - 2], dp_2[len(money) - 1])
    
    return answer

    # 방식
    # 1. 원형 배열이므로 처음 집과 마지막 집을 동시에 못 텀
    # 2. 두 경우로 나눠서 각각 DP 진행
        # 2-1. dp1: 첫 집 포함 가능, 마지막 집 제외 (money[0 ~ n-2])
        # 2-2. dp2: 첫 집 제외, 마지막 집 포함 가능 (money[1 ~ n-1])
    # 3. 점화식: dp[i] = max(dp[i-1], dp[i-2] + money[i])
    # 4. max(dp1 결과, dp2 결과) 반환