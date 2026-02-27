# 프로그래머스: 입국심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    
    # 최소 걸리는 시간 ~ 최대 걸리는 시간
    low, high = 1, max(times) * n
    
    while low <= high:
        # 중간 시간
        mid = (low + high) // 2       
        
        # check
        total = sum(mid // t for t in times)
        if total >= n:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
        
    return answer

    # 방식
    # 1. 이분 탐색으로 시간의 최솟값을 탐색
    # 2. low = 1, high = 가장 느린 입국심사관이 혼자 n명을 다 처리하는 시간(최악 case)
    # 3. mid분 동안 각 심사관이 처리 가능한 인원 (mid // t) total로 합산
        # 3-1. total >= n인 경우, 최솟값(answer) = mid로 하고, 최대한 시간 줄여보기 (high = mid - 1)
        # 3-2. 아닌 경우, low = mid + 1로 늘려 최솟값(answer) 탐색