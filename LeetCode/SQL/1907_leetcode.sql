-- LeetCode: Count Salary Categories
-- https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=top-sql-50

SELECT C.category, COUNT(A.category) AS accounts_count
FROM (
    SELECT "Low Salary" AS category 
    UNION SELECT "Average Salary" 
    UNION SELECT "High Salary" 
) C
LEFT JOIN (
    SELECT A1.account_id, A1.income, CASE WHEN A1.income < 20000 THEN "Low Salary" ELSE CASE WHEN A1.income <= 50000 THEN "Average Salary" ELSE "High Salary" END END AS category 
    FROM Accounts A1
) A
    ON C.category = A.category
    GROUP BY C.category

-- 회고
-- 1. 카테고리 테이블은 기존에 없는 내용이므로, UNION SELECT 서브쿼리로 생성
-- 2. LEFT JOIN 사용시 GROUP BY는 왼쪽 테이블 컬럼으로 해야 매칭이 안 된 경우에도 결과에 포함됨