-- LeetCode: Group Sold Products By The Date
-- https://leetcode.com/problems/group-sold-products-by-the-date/description/?envType=study-plan-v2&envId=top-sql-50

SELECT A2.sell_date, COUNT(A2.product) AS num_sold, GROUP_CONCAT(A2.product ORDER BY A2.product) AS products
FROM (
    SELECT DISTINCT A1.sell_date, A1.product
    FROM Activities A1
) A2
    GROUP BY A2.sell_date

-- 회고
-- 1. GROUP_CONCAT() 사용해 여러 값을 하나의 문자열로 합침
-- 2. GROUP_CONCAT(DISTINCT 컬럼 ORDER BY 컬럼)으로 중복 제거 및 정렬할 수 있음
-- 3. ORDER BY의 경우 타 집계함수는 값 하나라 필요없지만 GROUP_CONCAT은 여러 값을 다루기 때문에 가능