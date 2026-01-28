# 프로그래머스: 올바른 괄호의 갯수
# https://school.programmers.co.kr/learn/courses/30/lessons/12929

# 회고
# 1. 처음에 무조건 "("으로 나와야 하기 때문에, root에 "(" 고정
# 2. sub tree left node에 다음 "(", right node에 root node의 열린 괄호를 닫기 위한 ")"로 설정하고, dfs를 진행하면 될 줄 알았음.
# 3. test case 일부에서 계속 막혀, 푸는 방식을 찾아본 결과 백트래킹 방식으로 해야한다는 것을 확인
# 4. 문제 유형을 보고, 적절한 알고리즘 판별 기준을 정립할 필요가 있다고 생각함. (막 달려들지 말고)

def solution(n):
    answer, cur_str = [], []
    open_bracket, close_bracket = n, n
    
    def backtracking(str_list, open_cnt, close_cnt):
        # 종료 조건
        if len(str_list) == n * 2:
            answer.append(str_list[:])
            return 

        # 넣을 문자열이 ( 인 경우
        if open_cnt > 0:
            str_list.append("(")
            backtracking(str_list, open_cnt - 1, close_cnt)
            str_list.pop()
            #print(open_cnt - 1, close_cnt)
            
        # 넣을 문자열이 ) 인 경우
        if close_cnt > open_cnt:
            str_list.append(")")
            backtracking(str_list, open_cnt, close_cnt - 1)
            str_list.pop()
            #print(open_cnt, close_cnt - 1)
            
    backtracking(cur_str, open_bracket, close_bracket)
    
    # answer = 문자열 배열 
    result = len(answer)
    
    return result

    # 방식
    # 1. 열린 괄호와 닫힌 괄호 count를 각각 주어진 숫자 n개만큼 받음
    # 2. 백트래킹(브루트포스 + 가지치기)으로 진행해야하기 때문에 가지치기 수행(open_cnt > 0, close_cnt > open_cnt)
    # 3. 재귀 전 해당하는 괄호 append, 재귀 끝나고, 다른 case도 해야하므로, pop 진행
    # 4. length를 필요로 하기 때문에, len으로 거르고 출력