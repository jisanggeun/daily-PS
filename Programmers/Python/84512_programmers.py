# 프로그래머스: 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product

def solution(word):
    answer = 0
    
    result = []
    
    for l in range(1, 5 + 1):
        for p in product("AEIOU", repeat=l):
            result.append(''.join(p))
    
    result.sort()
    answer = result.index(word) + 1
    
    return answer

    # 방식
    # 1. "AEIOU" 5개 문자로 길이 1~5의 중복순열(product)을 생성
    # 2. 각 튜플을 join으로 문자열로 변환 후 리스트에 저장
    # 3. 사전순 정렬(sort) 후, word의 index를 찾아 +1 반환 (1-indexed)