# 프로그래머스: 모의고사
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    first_answer = [1,2,3,4,5]
    second_answer = [2,1,2,3,2,4,2,5]
    third_answer = [3,3,1,1,2,2,4,4,5,5]
    
    cnt = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == first_answer[i%len(first_answer)]:
            cnt[0] += 1
        if answers[i] == second_answer[i%len(second_answer)]:
            cnt[1] += 1
        if answers[i] == third_answer[i%len(third_answer)]:
            cnt[2] += 1
            
    max_num = max(cnt)
            
    for i in range(len(cnt)):
        if(max_num == cnt[i]):
            answer.append(i+1)
            
    return answer

    # 방식
    # 1. 수포자 1,2,3 각각 사이클이 있으므로, 사이클에 맞는 answer 미리 list에 입력
    # 2. 정답을 맞춘 count도 저장해야하므로, cnt list에 초기화
    # 3. 정답 확인 (for 문 answers length 만큼 반복)
    # 4. 정답을 가장 많이 맞춘 count 찾고, 그 count 만큼 진행한 수포자 찾아 answer에 append 진행