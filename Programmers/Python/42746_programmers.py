# 프로그래머스: 가장 큰 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    compare = []
    
    for i in range(len(numbers)):
        compare.append(str(numbers[i])*3)
    
    # 큰 순서대로
    compare.sort(reverse=True)
    
    for i in range(len(compare)):
        ori_len = len(compare[i]) // 3
        answer += compare[i][:ori_len]
        
        '''
        ori_len = len(compare[i]) / 3
        answer += compare[i][0:int(ori_len)]
        '''
    
    return str(int(answer))

    # 방식
    # 1. numbers 배열의 len만큼 compare 하기 위한 배열에 append 시키는데, 원소는 0 이상 1000 이하임
    # 2. compare 배열에 numbers 배열 인자를 넣을 때, 문자열로 바꾸고 *3(길이 3배)로 늘림 (원소 범위 때문 + 서로 다른 길이의 문자열)
    # 3. (ex. '989' vs '9') == '989' > '9' / (ex. '989989989' vs '999') == '989989989' < '999'
    # 4. 큰 수를 뽑아내야하므로, reverse = True 한 채로 sort 진행
    # 5. 다시 원래 값을 뽑아내야 하므로, len(compare)에서 // 3을 해, 원래 length를 받아온 후 compare 배열에서 0~원래 length만큼 값 가져와 answer에 저장
    # 6. [0, 0, 0 .., 0]과 같은 케이스 때문에 answer을 int로 감싼 후 다시 str로 감싸서 0000...0과 같은 값들을 0으로 출력하게 함. 

# lambda 사용
def solution(numbers):
    answer = ''

    compare = list(map(lambda x: str(x)*3, numbers))

    compare.sort(reverse=True)

    answer = ''.join(map(lambda x: x[:len(x)//3], compare))

    return str(int(answer))
