# 프로그래머스: 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    answer = 0
    nums = set()
    
    for l in range(1, len(numbers) + 1):
        for p in permutations(numbers, l):
            num = int(''.join(p))
            nums.add(num)
    
    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    
    is_prime[0], is_prime[1] = False, False
    
    # 에라토스테네스의 체
    for i in range(2, int(max_num**0.5) + 1):
        for j in range(i*2, max_num + 1, i):
            is_prime[j] = False
            
    for num in nums:
        if is_prime[num] == True:
            answer += 1

    return answer

    # 방식
    # 1. numbers의 각 숫자를 길이 1~len까지 순열(permutations)로 조합하여 가능한 모든 수 생성
    # 2. set으로 중복 제거 후, 최댓값 기준으로 에라토스테네스의 체로 소수 판별 배열 생성
    # 3. 생성된 수들 중 소수인 것만 카운트하여 반환