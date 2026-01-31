# 프로그래머스: H-index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

# 회고
# 1. 문제를 제대로 이해하지 않고 h-index를 인용횟수라 착각해 간단하게 계산하려 len(citations) - i로 계산한 점
# 2. 반례 케이스를 먼저 떠올리지 않고 비슷한 테스트 케이스만 입력 후 테스트 한 점
# 3. for문이 모든 경우를 커버하는지 확인 제대로 안한 점

def solution(citations):
    # citations's length == 논문 편수
    # citations's 인용 횟수 == citations[index]
    
    # 처음에 정렬 
    # [0,1,3,5,6] / [0,1,2,5,6] / [0,1,4,5,6]
    citations.sort()
    
    # h-index != citations[index] (인용 횟수)
    # h-index == 논문 편수
    h_candidate = 0
    for i in range(len(citations)):
        h_count = 0
        for j in range(len(citations)):
            if h_candidate <= citations[j]:
                h_count += 1
        if h_candidate == h_count: 
            return h_candidate
        elif h_candidate > h_count:
            return h_candidate - 1
        h_candidate += 1
            
    return len(citations)

    # 방식
    # 1. 맨 처음에 논문 인용 수는 랜덤 값이 들어가기 때문에, 이를 순서에 맞게 sorting 진행
    # 2. 그 이후 h_candidate(h-index가 될 수 있는지 확인하려는 값)랑 h_count(h_candidate번 이상 인용된 논문 편수)를 0으로 초기화 진행
    # 3. h_candidate과 citations[j](논문 인용 횟수) 값 비교 후 작거나 같으면 h_count ++
    # 4. 한 citation 반복 후 h_candidate와 h_count 비교해서, 같으면 그대로 h_candidate return
    # 5. h_candidate > h_count면, h_candidate - 1 return
    # 6. 이후 반복문이 끝나면 결국 h_candidate < h_count가 계속 유지됐으므로, h_candidate편 이상 인용된 논문이 h_candidate보다 많음
    # 7. 다만, len(citation)이 끝났기 때문에 따라서, len(citations) 반환

# for문의 i를 사용 안하는데, 이를 개선
def solution(citations):
    # citations's length == 논문 수
    # citations's 인용 횟수 == citations[index]
    
    # 처음에 정렬 
    # [0,1,3,5,6] / [0,1,2,5,6] / [0,1,4,5,6]
    citations.sort()
    
    # h-index != citations[index] (인용 횟수)
    # h-index == 논문 편수
    for h_candidate in range(len(citations) + 1):
        h_count = 0
        for j in range(len(citations)):
            if h_candidate <= citations[j]:
                h_count += 1
        if h_candidate == h_count: 
            return h_candidate
        elif h_candidate > h_count:
            return h_candidate - 1
            
    return len(citations)