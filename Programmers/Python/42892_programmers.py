# 프로그래머스: 길 찾기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/42892

# python 재귀 호출 제한 늘리기
import sys
sys.setrecursionlimit(10000)

def solution(nodeinfo):
    new_nodes = []
    
    for i in range(len(nodeinfo)):
        node_x, node_y = nodeinfo[i]
        node_num = i + 1
        
        new_nodes.append([node_num, node_x, node_y])
        
    new_nodes.sort(key=lambda x:(-x[2], x[1]))
    
    preorder = []
    postorder = []
    
    def dfs(nodes):
        # 종료 조건
        if nodes == []:
            return
        
        # 각 sub tree의 root node 생성 
        root = nodes[0]
        root_x = root[1]
        
        # 전위 탐색
        preorder.append(root[0])
        
        left = []
        right = []
        
        # sub tree의 left node
        for i in nodes[1:]:
            if i[1] < root_x:
                left.append(i)
                
        # sub tree의 right node
        for i in nodes[1:]:
            if i[1] > root_x:
                right.append(i)
        
        dfs(left)
        dfs(right)
        
        # 후위 탐색
        postorder.append(root[0])
    
    dfs(new_nodes)
                    
    answer = [preorder, postorder]
    return answer

    # 방식
    # 1. 일단 node 좌표를 받고, index를 합쳐 노드 재구성
    # 2. bst이므로, 요구하는 조건에 맞게 정렬 진행
    # 3. 각 sub tree의 root, left, right 노드 구성
    # 4. 조건에 맞게 preorder, postorder 진행 후 결과 출력
    # (번외. 파이썬 재귀 호출은 1000번으로, 테스트케이스에서 런타임 에러 발생 --> setrecursionlimit을 10000으로 올려 해결)