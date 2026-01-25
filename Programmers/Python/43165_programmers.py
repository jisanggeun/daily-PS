# 프로그래머스: 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3

def dfs(numbers, target, current):
    global answer
    
    if current == target and len(numbers) == 0:
        answer += 1
        return
    elif len(numbers) == 0:
        return
    
    num = numbers.pop()
    
    # left
    dfs(numbers, target, current - num)
    
    
    # right
    dfs(numbers, target, current + num)
    numbers.append(num)   
    
    return
    

def solution(numbers, target):
    global answer
    answer = 0
    
    dfs(numbers, target, 0)
    
    return answer

    # 방식
    # 1. Tree 세우기 
    # 2. dfs로 탐색
    # 3. 결과와 leaf 노드끼리 비교 후 리턴
    