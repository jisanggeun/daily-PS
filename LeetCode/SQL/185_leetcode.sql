-- LeetCode: Department Top Three Salaries
-- https://leetcode.com/problems/department-top-three-salaries/description/?envType=study-plan-v2&envId=top-sql-50

SELECT D.name AS Department, E2.name AS Employee, E2.salary AS Salary
FROM (
    SELECT E1.name, E1.departmentId, E1.salary, DENSE_RANK() OVER (PARTITION BY E1.departmentId ORDER BY E1.salary DESC) AS salary_rank
    FROM Employee E1
        ORDER BY E1.departmentId
) E2 
INNER JOIN Department D
    ON E2.departmentId = D.id
    WHERE E2.salary_rank <= 3

-- 회고
-- 1. RANK(), DENSE_RANK() = 윈도우 함수, 인자 없이 사용함
-- 2. rank 기준은 OVER (ORDER BY) 로 지정
-- 3. RANK() = 동점 시 순위 건너 뜀 (1, 2, 2, 4) / DENSE_RANK() = 동점 시 순위 건너뛰지 않음 (1, 2, 2, 3)
-- 4. PARTITION BY로 그룹 별 rank 매길 수 있음