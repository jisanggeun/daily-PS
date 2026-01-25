# 프로그래머스: 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    row, col = len(maps), len(maps[0])
    visit = [[False] * col for _ in range(row)]
    
    q = deque()
    
    visit[0][0] = True
    answer = 1
    
    q.append([0, 0, answer])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while len(q) != 0:
        cur_row, cur_col, cur_answer = q.popleft() 
        
        if cur_row == row - 1 and cur_col == col - 1:
            return cur_answer
            
        # 인접 노드
        for dr, dc in directions:
            nr, nc = cur_row + dr, cur_col + dc
            if 0 <= nr < row and 0 <= nc < col:
                if maps[nr][nc] == 1 and visit[nr][nc] == False:
                    visit[nr][nc] = True
                    q.append([nr, nc, cur_answer + 1])
                
    return -1

    # 방식 (최적화 및 개선)
    # 1. 전역 변수 사용 줄임
    # 2. directions 추가로, 코드 가독성 상승 

''' 
from collections import deque

def solution(maps):
    row, col = len(maps), len(maps[0])
    visit = [[False] * col for _ in range(row)]
    
    q = deque()
    
    visit[0][0] = True
    answer = 1
    
    q.append([0, 0, answer])
    
    while len(q) != 0:
        cur_row, cur_col, cur_answer = q.popleft() 
        
        if cur_row == row - 1 and cur_col == col - 1:
            return cur_answer
            
        # 인접 노드
        if cur_row > 0:
            if maps[cur_row - 1][cur_col] == 1 and visit[cur_row - 1][cur_col] == False:
                visit[cur_row - 1][cur_col] = True
                q.append([cur_row - 1, cur_col, cur_answer + 1])
        if cur_row < len(maps) - 1:
            if maps[cur_row + 1][cur_col] == 1 and visit[cur_row + 1][cur_col] == False:
                visit[cur_row + 1][cur_col] = True
                q.append([cur_row + 1, cur_col, cur_answer + 1])
        if cur_col > 0:
            if maps[cur_row][cur_col - 1] == 1 and visit[cur_row][cur_col - 1] == False:
                visit[cur_row][cur_col - 1] = True
                q.append([cur_row, cur_col - 1, cur_answer + 1])
        if cur_col < len(maps[0]) - 1:
            if maps[cur_row][cur_col + 1] == 1 and visit[cur_row][cur_col + 1] == False:
                visit[cur_row][cur_col + 1] = True
                q.append([cur_row, cur_col + 1, cur_answer + 1])   
                
    return -1
'''
    # 방식
    # 1. deque 사용해서, queue 사용 - (list로 받아서, 상태 업데이트 가능하게 구현)
    # 2. 인접 노드 상하좌우 고려 조건문 작성 
    # 3. return 조건 명확히 
    # (loop 내에선 특정 좌표 도달 시)
    # (loop 밖에선 특정 좌표 도달 못했단 뜻이므로, -1 return)