# 프로그래머스: 최소직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):    
    convert = sizes
    
    # max값 구하기 (현재 가로 세로 다 섞여 있음)
    max_x, max_y = max(size[0] for size in sizes), max(size[1] for size in sizes)
    
    # 뒤집기
    for i in range(len(convert)):
        x, y = convert[i]
        if x < y:
            convert[i] = [y, x]
            
    # print(convert_w)
    max_cx, max_cy = max(c[0] for c in convert), max(c[1] for c in convert)
        
    
    return max_cx * max_cy

    
    # 방식
    # 1. 가로 세로 값이 중구난방으로 섞여있는 테스트케이스에서 max값 (x,y)를 뽑아옴
    # 2. 가로 > 세로인 경우로 맞춰줘야 하므로, 가로 < 세로 값들 다 값 바꿔줌
    # 3. return 값 반환