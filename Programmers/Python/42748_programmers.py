# 프로그래머스: K번째수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

# sorted(), .sort() 둘 다 사용해서 구현

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start, end, index = commands[i]
        
        # 정렬된 새 list 사용
        answer.append(sorted(array[start-1:end])[index-1])

    return answer

    # 방식
    # 1. sorted()의 경우 새 list를 만들기 때문에, 다음 반복에 영향을 주지 않음 (대신 메모리 많이 사용)
    # 2. sorted(array[start-1:end]) 통해 array 뽑아낸 후 바로 sort 진행하고, 새 list에 저장
    # 3. 새 list[index-1](index 번째 요소)를 answer에 append

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start, end, index = commands[i]
        sort_array = array[start-1:end] 
        
        # 원본 리스트 자체를 변경
        sort_array.sort() 
        answer.append(sort_array[index-1])

    return answer

    # 방식
    # 1. .sort()의 경우 원본 리스트 자체를 변경하기 때문에, 다음 반복에 영향이 갈 수 있음
    # 2. 따라서, sort_array라는 새로운 변수에 array[start-1:end]까지 내용을 넣고 정렬시킴
    # 3. 그 이후 [index-1]번째 순서 append