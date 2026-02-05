-- LeetCode: The Number of Employees Which Report to Each Employee
-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=study-plan-v2&envId=top-sql-50

SELECT E1.employee_id, E1.name, COUNT(E2.age) AS reports_count, ROUND(AVG(E2.age), 0) AS average_age 
FROM Employees E1
INNER JOIN Employees E2
    ON E1.employee_id = E2.reports_to
    GROUP BY employee_id
    ORDER BY employee_id ASC

-- 회고
-- 1. employee_id는 unique_id이므로, name이랑 1대1 대응이므로, name에 어떤 값이 나올지 고정됨