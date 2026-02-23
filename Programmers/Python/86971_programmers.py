# 프로그래머스: 전력망을 둘로 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for p1, p2 in wires:
        graph[p1].append(p2)
        graph[p2].append(p1)
    
    for p1, p2 in wires:
        visit = [False] * (n + 1)
        visit[p1] = True
        
        q = deque()
        q.append(p1)
        
        cnt = 1
        
        while q:
            cur_p = q.popleft()
            
            for nxt_p in graph[cur_p]:
                if visit[nxt_p] == True: # 이미 방문
                    continue
                if (cur_p == p1 and nxt_p == p2) or (cur_p == p2 and nxt_p == p1): # 끊은 edge
                    continue
                
                visit[nxt_p] = True
                q.append(nxt_p)
                
                cnt += 1
        
        diff = abs(cnt - (n - cnt))
        answer = min(diff, answer)
    
    return answer

    # 방식
    # 1. wires로 인접 리스트(graph) 생성 후, 간선을 하나씩 끊어보며 완전탐색
    # 2. 끊은 간선을 무시하고 BFS로 한쪽 그룹의 노드 수(cnt)를 카운트
    # 3. 두 그룹 차이 abs(cnt - (n - cnt))의 최솟값을 answer로 반환