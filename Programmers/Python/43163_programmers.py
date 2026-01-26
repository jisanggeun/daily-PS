# 프로그래머스: 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    visit = [False] * len(words)
    answer = 0

    q = deque()
    q.append([begin, answer])
    
    while len(q) != 0:
        cur_word, cur_answer = q.popleft()
        
        # 종료 조건 
        if cur_word == target:
            return cur_answer
        
        # 인접 노드 찾아야 하는데, 인접 노드 = 한 개의 알파벳으로 바꿀 수 있는 단어
        for i in range(len(words)):
            diff_cnt = 0
            for j in range(len(cur_word)):
                if cur_word[j] != words[i][j]:
                    diff_cnt += 1
            # 인접 노드 방문
            if diff_cnt == 1 and visit[i] == False:
                visit[i] = True
                q.append([words[i], cur_answer+1])
                
        
    return answer
    
    # 방식
    # 1. 최소 return이니까 bfs 사용
    # 2. bfs 이므로, deque 라이브러리로 queue 이용
    # 3. 인접 노드 방문 조건 = cur_word에서 한 개의 알파벳을 바꾼 것과 word list의 단어 매치
    # 4. diff_cnt라는 변수로 다른 부분 cnt 후 1개만 다를 경우(cnt == 1 인 경우) 인접 노드로 방문 처리
    # 5. 종료 조건에 만족한 경우(target과 cur_word가 동일한 경우) return