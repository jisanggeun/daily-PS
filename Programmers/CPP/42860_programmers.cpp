// 프로그래머스: 조이스틱
// https://school.programmers.co.kr/learn/courses/30/lessons/42860

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string name) {
    int answer = 0;
    string start(name.size(), 'A');
    
    // 앞 뒤
    int move = name.size() - 1; // 최악
    
    for(int i = 0; i < name.size(); i++) {
        int next = i + 1;
        
        while(next < name.size() && name[next] == 'A') next++; // i번째 다음 연속된 A 구간
        
        
        move = min(move, i * 2 + (int)(name.size() - next));
        move = min(move, (int)(name.size() - next) * 2 + i);
    }
    
    // 위 아래 합산
    for(int i = 0; i < name.size(); i++) {
        if(start[i] == name[i]) continue;
        else {
            int up = name[i] - 'A'; // 위로 가는 거리
            int down = 26 - up; // 알파벳 총 개수 - 위로 가는 거리 = 아래로 가는 거리
            answer += min(up, down);
        }
    }
    
    return answer + move;
}

// 방식
// 1. A가 아닌 문자를 전부 방문하는 최소 이동 횟수 + 각 문자를 A로부터 위, 아래 중 짧은 방향으로 변환하는 횟수
// 2. A가 아닌 문자를 전부 방문하는 최소 이동 횟수
    // 2-1. A는 방문 안해도 되니, 연속된 A 문자 구간 피해서 돌아가기.
    // 2-2. 최악 구하고, 연속된 문자 구해서, 오른쪽 먼저 갔다 되돌아 왼쪽으로 가는거, 왼쪽 먼저 갔다 되돌아 오른쪽으로 가는거랑 비교해 최소값만 가져옴
// 3. 각 문자를 A로부터 위, 아래 중 짧은 방향으로 변환하는 횟수
    // 3-1. name[i]에서 A를 뺀 값(위로 가는 거리)와 알파벳 총 개수에서 위로 가는 거리 뺀 값(아래로 가는 거리) 중 최소를 answer에 더함
// 4. 2와 3에서 나온 값들 더함

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string name) {
    int answer = 0;
    string start(name.size(), 'A');
    
    // 앞 뒤
    int move = name.size() - 1; // 최악
    
    for(int i = 0; i < name.size(); i++) {
        int next = i + 1;
        
        while(next < name.size() && name[next] == 'A') next++; // i번째 다음 연속된 A 구간
        
        
        move = min(move, i * 2 + (int)(name.size() - next));
        move = min(move, (int)(name.size() - next) * 2 + i);
    }
    
    // 위 아래 합산
    for(int i = 0; i < name.size(); i++) {
        if(start[i] == name[i]) continue;
        else {
            if(name[i] > 'N') {
                start[i] = 'Z';
                answer++;
            }
            while(start[i] != name[i]) {
                if(name[i] > 'N') start[i]--;
                else start[i]++;
                
                answer++;
            }
        }
    }
    
    return answer + move;
}

// 각 문자를 A로부터 위, 아래 중 짧은 방향으로 변환하는 횟수
    // 정 가운데인 N을 기준으로 아래 위로 갈지 판단 후, answer++