-- LeetCode: Replace Employee ID With The Unique Identifier
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/?envType=study-plan-v2&envId=top-sql-50

SELECT EmployeeUNI.unique_id, Employees.name FROM Employees LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;

-- 회고
-- 1. 어느 쪽 기준으로 데이터가 전부 필요한지 생각해보기. (left, right, outer 일 때)