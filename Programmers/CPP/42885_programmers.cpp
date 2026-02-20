// 프로그래머스: 구명보트
// https://school.programmers.co.kr/learn/courses/30/lessons/42885

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    
    sort(people.begin(), people.end());
    
    int left = 0;
    int right = people.size() - 1;
    
    while(left <= right) {
        if(people[left] + people[right] <= limit) left++;
        right--;
        answer++;
    }
    
    return answer;
}

// 방식
// 1. 처음에 sort 먼저 진행해서 오름차순으로 만듬
// 2. left = 처음, right = 끝 해서 2 pointer로 구현
    // 2-1. left <= right일때 반복되도록 설정 후 left 번째와 right 번째 값 합쳐서 limit보다 작거나 같으면 left가 올라가게,
    // 2-2. 아닌 경우 right값이 커서, limit안에 속하지 않았으므로, right가 내려가게,
// 3. answer++ 진행 

// 최적화 전 코드
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    
    sort(people.begin(), people.end());
    
    int left = 0;
    int right = people.size() - 1;
    
    while(left <= right) {
        if(people[left] + people[right] <= limit) {
            if(people[left] == -1 || people[right] == -1) {
                right--;
                continue;
            }
            
            people[left] = -1;
            people[right] = -1;
            answer++;
            left++;
            right--;
        } else {
            right--;
        }
    }
    
    for(int i = 0; i < people.size(); i++) {
        if(people[i] == -1) continue;
        answer++;
    }
    
    return answer;
}
