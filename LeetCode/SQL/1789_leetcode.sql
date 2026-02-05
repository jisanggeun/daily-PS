-- LeetCode: Primary Department for Each Employee
-- https://leetcode.com/problems/primary-department-for-each-employee/description/?envType=study-plan-v2&envId=top-sql-50

SELECT E2.employee_id, E2.department_id
FROM Employee E2
INNER JOIN (
    SELECT E1.employee_id, COUNT(department_id) AS cnt_dep 
    FROM Employee E1
        GROUP BY E1.employee_id
) E3
    ON E2.employee_id = E3.employee_id
    WHERE (E2.primary_flag = "Y") OR (E3.cnt_dep = 1)

-- 회고
-- 1. (E2.primary_flag = "Y" AND E3.cnt_dep > 1)를 더 줄일 수 있음 
-- 2. 부서가 1개면 flag 상관없이 출력이고, 2개 이상이면 flag가 Y일 때인데, 부서가 1개가 아니면 이미 2개 이상이란 뜻이므로 E3.cnt_dep > 1를 없앨 수 있음