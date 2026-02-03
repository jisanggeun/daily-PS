-- LeetCode: Project Employees I
-- https://leetcode.com/problems/project-employees-i/description/?envType=study-plan-v2&envId=top-sql-50

SELECT P.project_id, ROUND(SUM(E.experience_years) / COUNT(E.employee_id), 2) AS average_years 
FROM Project P 
INNER JOIN Employee E 
    ON P.employee_id = E.employee_id 
    GROUP BY P.Project_id;

-- 회고
-- 1. 예외 처리 하란 조건이 없었기 때문에 NULL값 고려 안 해도 되므로, INNER JOIN 진행
-- 2. 개선점: experience_year를 항 개수에 따라 나누므로, SUM(E.experience_years) / COUNT(E.employee_id) 역시 AVG(E.experience_years)로 바꾸면 더 간단해짐

SELECT P.project_id, ROUND(AVG(E.experience_years), 2) AS average_years
FROM Project P
INNER JOIN Employee E
    ON P.employee_id = E.employee_id
    GROUP BY P.Project_id;