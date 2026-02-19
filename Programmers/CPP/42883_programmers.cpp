// 프로그래머스: 큰 수 만들기
// https://school.programmers.co.kr/learn/courses/30/lessons/42883

#include <string>
#include <vector>
#include <iostream>
#include <stack>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    
    string s;
    int i = 0;
    
    s.push_back(number[i++]);
    
    while(i < number.size()) {
        while(s.size() != 0 && s.back() < number[i] && k > 0) {
            s.pop_back();
            k--;
        }
        s.push_back(number[i++]);
    }
    
    while(k > 0) {
        s.pop_back();
        k--;
    }
    
    answer = s;
    
    return answer;
}

// 방식
// 1. string을 스택처럼 활용 (push_back, pop_back, back)
    // 1-1. (string, stack) push_back = push, pop_back = pop, back = top
// 2. 앞에서부터 숫자를 하나씩 봄
    // 2-1. 스택 top이 현재 숫자보다 작으면, pop (k--)
    // 2-2. while로 연속 제거 (if 사용 시 한 번만 제거되므로, 안 됨)
    // 2-3. 현재 숫자 push
// 3. 다 돌았는데 k가 아직도 남아있으면 (k > 0)일때, 뒤에서 k 제거 
    // 3-1. 해당하는 케이스 = 내림차순 (ex. 54321, k = 2)