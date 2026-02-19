// 프로그래머스: 체육복
// https://school.programmers.co.kr/learn/courses/30/lessons/42862

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());
    
    answer = n - lost.size();
    
    // 중복 제거
    for(int i = 0; i < lost.size(); i++) {
        for(int j = 0; j < reserve.size(); j++) {
            if(reserve[j] == lost[i]) {
                reserve[j] = -1;
                lost[i] = -1;
                answer++;
                break;
            }
        }
    }
    
    // 앞 뒤 
    for(int i = 0; i < lost.size(); i++) {
        for(int j = 0; j < reserve.size(); j++) {
            if(reserve[j] == lost[i] - 1 || reserve[j] == lost[i] + 1) {
                reserve[j] = -1;
                answer++;
                break;
            }
        }
    }
    
    return answer;
}

// 방식
// 1. answer = n - 잃어버린 사람의 수로 시작
// 2. 여벌 체육복을 가져왔으나, 도난당했으면 빌려주지 못하고 자기가 입어야하기 때문에, 중복 제거 (따라서, answer++ 가능 (잃어버리지 않았기 때문))
// 3. 이후 여벌 체육복을 앞 뒤로 greedy하게 나눠주기 때문에 나눠줄때마다 answer++
