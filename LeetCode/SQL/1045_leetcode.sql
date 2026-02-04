-- LeetCode: Customers Who Bought All Products
-- https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=study-plan-v2&envId=top-sql-50

SELECT C.customer_id
FROM (
    SELECT C1.customer_id, COUNT(DISTINCT C1.product_key) AS cnt_buy_prod, (SELECT COUNT(P.product_key) FROM Product P) AS cnt_prod
    FROM Customer C1 
        GROUP BY C1.customer_id 
) C
    WHERE C.cnt_buy_prod = C.cnt_prod

-- 회고
-- 1. 문제 조건 제대로 확인하기 (중요)
-- 2. 중복 가능하기 때문에 DISTINCT 사용 
-- 3. 서브 쿼리, JOIN 각각 사용

SELECT C.customer_id
FROM (
    SELECT C1.customer_id, COUNT(DISTINCT C1.product_key) AS cnt_buy_prod
    FROM Customer C1 
        GROUP BY C1.customer_id 
) C 
INNER JOIN (
    SELECT COUNT(P1.product_key) AS cnt_prod
    FROM Product P1
) P
ON C.cnt_buy_prod = P.cnt_prod