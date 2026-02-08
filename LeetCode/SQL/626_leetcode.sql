-- LeetCode: Exchange Seats
-- https://leetcode.com/problems/exchange-seats/description/?envType=study-plan-v2&envId=top-sql-50

SELECT S2.id, CASE WHEN S2.student IS NOT NULL THEN S2.student ELSE S3.student END AS student
FROM Seat S3
INNER JOIN (
    SELECT S1.id, CASE WHEN S1.id % 2 = 0 THEN LAG(S1.student, 1) OVER (ORDER BY S1.id) ELSE LEAD(S1.student, 1) OVER (ORDER BY S1.id) END AS student
    FROM Seat S1
) S2
    ON S2.id = S3.id;

-- 회고
-- 1. 윈도우 함수 접근 및 활용을 잘해야 할 듯 함
-- 2. JOIN에서 ON 부분 CASE문은 값 반환용으로만 사용 가능, 조건문으로는 사용 불가
-- 3. NULL 비교는 = 로 안되기 때문에 IS NULL 사용해야 함 
-- 3-1. (홀수면 마지막 S2.student가 NULL인데, S2.student = S3.student 하면, NULL = S3.student가 되므로 안 됨)

