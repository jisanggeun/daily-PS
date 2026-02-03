-- LeetCode: Managers with at Least 5 Direct Reports
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&envId=top-sql-50

SELECT t1.name 
FROM (
    SELECT COUNT(E1.managerId) AS M_Count, E2.id, E2.name 
    FROM Employee E1 
    INNER JOIN Employee E2 
        ON E1.managerId = E2.id 
        GROUP BY E1.managerId
) t1 
WHERE t1.M_Count >= 5 

-- 회고
-- 1. SELF JOIN으로 동일 table 복사 후 INNER JOIN
-- 2. managerId의 count가 5 이상인 name을 SELECT 하도록 구현
-- 3. 개선점: HAVING 사용하면 더 간단하게 구현될 듯함

SELECT E2.name
FROM Employee E1 
INNER JOIN Employee E2
    ON E1.managerID = E2.id
    GROUP BY E1.managerID
    HAVING COUNT(E1.managerID) >= 5