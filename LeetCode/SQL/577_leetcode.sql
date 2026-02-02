-- LeetCode: Employee Bonus
-- https://leetcode.com/problems/employee-bonus/description/?envType=study-plan-v2&envId=top-sql-50

SELECT E.name, B.bonus FROM Employee E LEFT JOIN Bonus B ON E.empId = B.empId WHERE B.bonus is NULL OR B.bonus < 1000;

-- 회고
-- 1. LEFT JOIN하는데, 교집합 부분 전부 참조하지 않고 일부만 참조하기 때문에 OR 연산자를 통해 부분만 추가 참조 구현