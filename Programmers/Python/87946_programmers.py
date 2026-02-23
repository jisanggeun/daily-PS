# 프로그래머스: 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons):
        remain = k
        cnt = 0
        for min_cost, cost in p:
            if remain >= min_cost:
                remain -= cost
                cnt += 1
                
        answer = max(answer, cnt)

            
    return answer

    # 방식
    # 1. 던전 배열의 모든 순열(permutations)을 생성하여 가능한 방문 순서를 전부 탐색 진행
    # 2. 각 순열마다 피로도(remain)를 차감하며 입장 가능한 던전 수(cnt)를 카운트
    # 3. 모든 순열 중 최대 cnt를 answer로 반환