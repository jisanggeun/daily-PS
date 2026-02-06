-- LeetCode: Last Person to Fit in the Bus
-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/?envType=study-plan-v2&envId=top-sql-50

SELECT Q2.person_name
FROM (
    SELECT Q1.turn, Q1.person_id, Q1.person_name, Q1.weight, SUM(Q1.weight) OVER(ORDER BY Q1.turn) AS total_weight
    FROM Queue Q1
) Q2
    WHERE Q2.total_weight <= 1000
    ORDER BY total_weight DESC
    LIMIT 1

-- 회고
-- 1. 윈도우 함수 SUM() OVER(ORDER BY)로 누적합 계산함
-- 2. 집계 함수 = 여러 행 -> 하나의 값, 윈도우 함수 = 여러 행 -> 각 행마다 값 (OVER() 붙으면 윈도우 함수임)
-- 3. 조건 만족하는 것 중 가장 큰 값을 가져와야하므로, ORDER BY DESC 후 LIMIT 1을 걸어 1개만 출력되게 함