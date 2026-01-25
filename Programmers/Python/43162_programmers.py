# 프로그래머스: 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    visit = [False] * n
    answer = 0
    
    def dfs(start):
        visit[start] = True
        
        for j in range(n):
            if computers[start][j] == 1 and visit[j] == False:
                dfs(j)
        
    for i in range(n):
        if visit[i] == False:
            answer += 1
            dfs(i)
        
    print(visit)
    
    return answer

    # 방식 (최적화 및 개선)
    # 1. 함수 안에 함수로 가독성 상승 및 전역 변수 선언 줄임
    # 2. dfs 시작할 때, answer ++로 변경 

'''
def dfs(n, computers, start):
    global answer;
    if visit[start] == True:
        return
    
    visit[start] = True
    # 이제 배열의 인접 노드 찾기.
    for j in range(n):
        if j == start:
            continue
        elif computers[start][j] == 1 and visit[j] == False:
            answer -= 1
            dfs(n, computers, j)
    
        

def solution(n, computers):
    global answer, visit
    answer = n
    
    visit = [False] * n;
    
    for i in range(n):
        dfs(n, computers, i)
    print(visit)
    
    return answer
'''

    # 방식
    # 1. 노드 수 = 네트워크 수 (최대, 아무 것도 연결되지 않았을 때)
    # 2. visit list는 방문 했는지 안했는지 판단하는 list
    # 3. dfs로 탐색 후 인접 노드 연결될 때마다 노드 수 감소