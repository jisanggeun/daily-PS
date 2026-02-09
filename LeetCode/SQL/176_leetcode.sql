-- LeetCode: Second Highest Salary
-- https://leetcode.com/problems/second-highest-salary/?envType=study-plan-v2&envId=top-sql-50

SELECT (
    SELECT DISTINCT E2.salary
    FROM (
        SELECT E1.salary, DENSE_RANK() OVER (ORDER BY E1.salary DESC) AS rank_salary
        FROM Employee E1
    ) E2 
    WHERE E2.rank_salary = 2
) AS SecondHighestSalary

-- 회고
-- 1. 결과가 없을 때 null return 하려면, SELECT (서브쿼리) AS 컬럼명 형태로 감싸면 됨
-- 2. DENSE_RANK()로 rank 매길 때 높은 순서로 해야하므로 ORDER BY DESC 사용
-- 3. 같은 rank가 여러 개일 수도 있으니 DISTINCT 또는 LIMIT 1 사용