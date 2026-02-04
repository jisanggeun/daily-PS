-- LeetCode: Product Sales Analysis III
-- https://leetcode.com/problems/product-sales-analysis-iii/description/?envType=study-plan-v2&envId=top-sql-50

SELECT S2.product_id, S2.year AS first_year, S2.quantity, S2.price 
FROM Sales S2 
INNER JOIN (
    SELECT S1.product_id, MIN(S1.year) AS check_year
    FROM Sales S1
        GROUP BY S1.product_id
) S3
ON S2.product_id = S3.product_id AND S2.year = S3.check_year

-- 회고 
-- 1. GROUP BY를 사용할 땐 GROUP BY에 사용할 컬럼명, 집계 함수 외 다른걸 쓰지 않기.