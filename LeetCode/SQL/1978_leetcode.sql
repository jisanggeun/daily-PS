-- LeetCode: Employees Whose Manager Left the Company
-- https://leetcode.com/problems/employees-whose-manager-left-the-company/description/?envType=study-plan-v2&envId=top-sql-50

SELECT E1.employee_id
FROM Employees E1
    WHERE E1.manager_id NOT IN (
        SELECT E2.employee_id
        FROM Employees E2
    )
    AND E1.manager_id IS NOT NULL 
    AND E1.salary < 30000
    ORDER BY E1.employee_id ASC

-- 회고
-- 1. WHERE 절에 서브쿼리 쓰는 게 익숙하지 않은데, 연습 필요
-- 2. NOT IN 사용 시 NULL 값 주의해야 함 (서브쿼리 결과에 NULL 있거나 비교할 대상이 NULL인 경우 결과 이상해짐)
-- 2-1. IS NOT NULL 사용으로 해결