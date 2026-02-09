-- LeetCode: List the Products Ordered in a Period
-- https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/?envType=study-plan-v2&envId=top-sql-50

SELECT P.product_name, SUM(O.unit) AS unit
FROM Products P
INNER JOIN Orders O
    ON P.product_id = O.product_id
    WHERE O.order_date > "2020-01-31"
    AND O.order_date < "2020-03-01"
    GROUP BY P.product_name
    HAVING unit >= 100

-- 회고
-- 1. HAVING은 GROUP BY 후 집계 결과에 조건 걸 때 사용
-- 2. WHERE = 집계 전 행 필터링 / HAVING = 집게 후 그룹 필터링