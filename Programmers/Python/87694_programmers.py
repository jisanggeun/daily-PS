# 프로그래머스: 아이템 줍기
# https://school.programmers.co.kr/learn/courses/30/lessons/87694

# 최소거리 = BFS
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 사각형 크기 지정 
    max_x = max(rect[2] for rect in rectangle)
    max_y = max(rect[3] for rect in rectangle)    
    
    visit = [[True] * (max_x * 2 + 1) for _ in range(max_y * 2 + 1)]
    
    # 네모 테두리 그리기
    for rect in rectangle:
        start_x, end_x = rect[0] * 2, rect[2] * 2
        start_y, end_y = rect[1] * 2, rect[3] * 2
        
        for x in range(start_x, end_x + 1):
            visit[start_y][x] = False
            visit[end_y][x] = False
            
        for y in range(start_y, end_y + 1):
            visit[y][start_x] = False
            visit[y][end_x] = False
        
    # 겹치는 네모 테두리 지우기 (사각형 내부 True로 채우기)   
    for rect in rectangle:
        start_x, end_x = rect[0] * 2, rect[2] * 2
        start_y, end_y = rect[1] * 2, rect[3] * 2
        
        for y in range(start_y + 1, end_y):
            for x in range(start_x + 1, end_x):
                visit[y][x] = True
            
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]        
            
    q = deque()
    q.append([characterX * 2, characterY * 2, answer])
    visit[characterY * 2][characterX * 2] = True
            
    while len(q) != 0:
        cur_x, cur_y, cur_answer = q.popleft()
        
        # 종료 조건
        if cur_x == itemX * 2 and cur_y == itemY * 2:
            return cur_answer // 2
        
        # 인접 노드 찾기
        for dx, dy in directions:
            nx, ny = cur_x + dx, cur_y + dy
            if 0 <= nx <= max_x * 2 and 0 <= ny <= max_y * 2:
                if visit[ny][nx] == False:
                    visit[ny][nx] = True
                    q.append([nx, ny, cur_answer + 1])
    
    return answer

    # 방식
    # 1. 최소 거리 -> bfs 사용
    # 2. bfs 이므로, deque 라이브러리로 queue 이용
    # 3. 최외각 경로만 따라 움직여야 하기 때문에 2를 곱함 (2 곱하지 않고 그대로 사용할 경우 테두리가 붙어있으면, 뚫고 지나가므로, 에러 생성)
    # 4. 네모 테두리 그리고, 사각형 내부 true로 채움 
    # 5. 인접 노드 방문 조건 = 상하좌우 중 false인 곳만
    # 6. 종료 조건에 만족한 경우(itemX * 2, itemY * 2 인 경우) return // 2 (2를 곱했으므로)