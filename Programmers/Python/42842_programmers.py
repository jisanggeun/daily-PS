# 프로그래머스: 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    color = brown + yellow
    
    for i in range(1, int(color**0.5) + 1):
        if color % i == 0:
            w, h = color // i, i
            if (w - 2) * (h - 2) == yellow:     
                    answer = [w, h]
            
    return answer

    # 방식
    # 1. 전체 컬러 수(brown + yellow)의 약수 쌍(w, h)을 root color까지 탐색
    # 2. 각 약수 쌍에서 테두리를 제외한 내부 영역 (w-2)*(h-2)가 yellow와 일치하는지 확인
    # 3. 조건 만족하는 [가로, 세로]를 반환