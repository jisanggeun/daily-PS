-- LeetCode: Restaurant Growth
-- https://leetcode.com/problems/restaurant-growth/description/?envType=study-plan-v2&envId=top-sql-50

SELECT C3.visited_on, C3.amount, C3.average_amount
FROM (
    SELECT C2.visited_on, SUM(C2.sum_amount) OVER (ORDER BY C2.visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS amount, ROUND(AVG(C2.sum_amount) OVER (ORDER BY C2.visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW), 2) AS average_amount
    FROM (
        SELECT C.visited_on, SUM(C.amount) AS sum_amount
        FROM Customer C
            GROUP BY C.visited_on
    ) C2
) C3
    WHERE C3.visited_on >= DATE_ADD((
        SELECT MIN(C4.visited_on)
        FROM Customer C4
    ), INTERVAL 6 DAY)

-- 회고
-- 1. 윈도우 함수에서 ROWS = 행 개수 기준, RANGE = 실제 값 범위 기준
-- 1-1. 매일 최소 한 명의 고객이 있음 (there will be at least one customer every day)
-- 1-2. ROWS나 RANGE나 상관 없지만 RANGE가 문제 정의에 더 맞아보이므로, RANGE 사용 
-- 1-3. (날짜 누락 존재 시 ROWS = 결과 달라짐, RANGE = 안 달라짐)
-- 2. RANGE BETWEEN INTERVAL N DAY PRECEDING AND CURRENT ROW = N일 범위 SUM/AVERAGE 계산 가능
-- 3. 윈도우 함수 결과에 WHERE 조건 걸리면, 서브쿼리로 감싸야 함 (WHERE이 윈도우 함수보다 먼저 실행됨)
-- 4. 첫 날짜 후 N일 이후부터 출력하려면 DATE_ADD((SELECT MIN(날짜) FROM 테이블), INTERVAL N DAY)로 필터링 진행