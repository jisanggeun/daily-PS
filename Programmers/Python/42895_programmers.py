# 프로그래머스: N으로 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/42895

# 가독성 있는 답안
def solution(N, number):
    answer = -1
    
    dp = [set() for _ in range(9)]
    
    # dp[1] = {N} ... dp[8] = {NNNNNNNN}
    for i in range(1, 9):
        dp[i] = {int(str(N) * i)}
    
    for i in range(1, 9):
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b !=0: 
                        dp[i].add(a//b) # 나눗셈에서 나머지 무시
                    
    for i in range(1, 9):
        for x in dp[i]:
            if x == number:
                answer = i
                return answer
        
    return answer

    # 방식
    # 1. dp[i] = N을 i번 사용해서 만들 수 있는 모든 수의 set (NN....N 포함)
    # 2. dp[i]를 채울 때, dp[j] ⊕ dp[i-j] (j = 1 ~ i-1, j = i번째 이전까지) 사칙 연산의 결과를 모두 추가
        # 2-1. i=4일 때
        # 2-2. j = 1 => dp[1] ⊕ dp[3]
        # 2-3. j = 2 => dp[2] ⊕ dp[2]
        # 2-4. j = 3 => dp[3] ⊕ dp[1]
    # 3. i를 1부터 8까지 순서대로 채우고, i = 1부터 순회하며, number가 있을 시 즉시 return (최소 i값 보장됨)
    # 4. 8까지 돌고 못 찾을 시 -1 return

# 제출한 답안
def solution(N, number):
    answer = -1
    
    dp = [set() for _ in range(9)]
    
    # dp[1] = {N} ... dp[8] = {NNNNNNNN}
    for i in range(1, 9):
        dp[i] = {int(str(N) * i)}
        if number in dp[i]:
            answer = i
            return answer
    
    for i in range(1, 9):
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    if number in (a+b, a-b, a*b):
                        answer = i
                        return answer
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b !=0: 
                        if number == a//b:
                            answer = i
                            return answer
                        dp[i].add(a//b) # 나눗셈에서 나머지 무시                  

    return answer

    # 방식
    # 1. dp[i] = N을 i번 사용해서 만들 수 있는 모든 수의 set (NN....N 포함)
    # 2. dp[i]를 채울 때, dp[j] ⊕ dp[i-j] (j = 1 ~ i-1, j = i번째 이전까지) 사칙 연산의 결과를 모두 추가
        # 2-1. i=4일 때
        # 2-2. j = 1 => dp[1] ⊕ dp[3]
        # 2-3. j = 2 => dp[2] ⊕ dp[2]
        # 2-4. j = 3 => dp[3] ⊕ dp[1]
    # 3. i를 1부터 8까지 순서대로 채우고, number가 발견될 시 즉시 i return (최소 i값 보장됨)
    # 4. 8까지 돌고 못 찾을 시 -1 return