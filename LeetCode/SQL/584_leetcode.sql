-- LeetCode: Find Customer Referee
-- https://leetcode.com/problems/find-customer-referee/description/?envType=study-plan-v2&envId=top-sql-50

SELECT name FROM Customer WHERE referee_id IS NULL or referee_id != 2;

-- 회고
-- 1. referee_id가 id != 2만 인 경우 NULL도 나오지 않기 때문에 or 연산자를 사용해 NULL일 때도 나오게 함