// 프로그래머스: 단속카메라
// https://school.programmers.co.kr/learn/courses/30/lessons/42884

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 1;
    
    // 끝 시간 오름차순 정렬
    // [-20,-15], [-18,-13], [-14,-5], [-5,-3]
    sort(routes.begin(), routes.end(), [](auto& a, auto& b){
       return a[1] < b[1]; 
    });
    
    int idx = routes[0][1]; // 카메라 위치
    
    for(int i = 1; i < routes.size(); i++) {
        if(routes[i][0] > idx) {
            idx = routes[i][1];
            answer++;
        }
    }
    
    return answer;
}

// 방식
// 1. 끝 시간 기준 오름차순 정렬 진행
// 2. 첫 차 나간 시점에 카메라 설치 (따라서, answer = 1 시작)
// 3. 앞에서부터 하나씩 보면서
    // 3-1. 진입 시점이 카메라 위치보다 뒤에 있으면 카메라 새로 설치해야하므로, answer++
    // 3-2. 아니면 기존 카메라에 걸리기 때문에 skip