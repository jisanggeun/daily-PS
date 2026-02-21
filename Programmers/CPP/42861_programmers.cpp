// 프로그래머스: 섬 연결하기
// https://school.programmers.co.kr/learn/courses/30/lessons/42861

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int parent[100];

int find(int x) {
    if(parent[x] != x) parent[x] = find(parent[x]);
    return parent[x];
}

void union_(int start, int end) {
    int a = find(start);
    int b = find(end);
    
    if(a < b) parent[b] = a;
    else parent[a] = b;
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    
    sort(costs.begin(), costs.end(), [](auto& a, auto& b) {
        return a[2] < b[2];
    });
    
    for(int i = 0; i < n; i++) {
        parent[i] = i;
    }
    
    for(int i = 0; i < costs.size(); i++) {
        int start = costs[i][0];
        int end = costs[i][1];
        int cost = costs[i][2];
        
        if(find(start) != find(end)) {
            union_(start, end);
            answer += cost;
        }
    }
    
    return answer;
}

// 방식
// 1. 크루스칼 사용
// 2. parent 배열 초기화 진행
// 3. 작은 edge부터 하나씩 확인
    // 3-1. find로 두 노드의 parent 확인
    // 3-2. parent 다를 시, 사이클이 아니므로, union으로 연결 진행 (answer += cost)
    // 3-3. parent 같을 시, 이미 연결됐기 때문에 skip