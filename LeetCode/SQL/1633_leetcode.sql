-- LeetCode: Percentage of Users Attended a Contest
-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/?envType=study-plan-v2&envId=top-sql-50

SELECT R.contest_id, ROUND(COUNT(R.user_id) / (
    SELECT COUNT(user_id) 
    FROM Users) * 100, 2) AS percentage
FROM Users U 
INNER JOIN Register R 
    ON U.user_id = R.user_id 
    GROUP BY R.contest_id
    ORDER BY percentage DESC, R.contest_id ASC;

-- 회고
-- 1. join으로 매칭시키고, R.contest_id로 그루핑 한 user 행에서 원본 user 전체 행을 나눔
-- 2. 개선점: join 사용 안 해도 구현 가능

SELECT R.contest_id, ROUND(COUNT(R.user_id) / (
    SELECT COUNT(U.user_id) 
    FROM Users U) * 100, 2) AS percentage
FROM Register R
    GROUP BY R.contest_id
    ORDER BY percentage DESC, R.contest_id ASC