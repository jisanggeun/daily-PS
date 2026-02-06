-- LeetCode: Product Price at a Given Date
-- https://leetcode.com/problems/product-price-at-a-given-date/description/?envType=study-plan-v2&envId=top-sql-50

SELECT P5.product_id, CASE WHEN P4.new_price IS NULL THEN 10 ELSE P4.new_price END AS price
FROM (
    SELECT P3.product_id, P3.change_date 
    FROM Products P3
        GROUP BY P3.product_id
) P5
LEFT JOIN (
    SELECT P1.product_id, P1.new_price
    FROM Products P1
        WHERE P1.change_date = (
            SELECT MAX(P2.change_date) 
            FROM Products P2
                WHERE P2.product_id = P1.product_id
                AND P2.change_date <= "2019-08-16"
        )
) P4
    ON P4.product_id = P5.product_id;

-- 회고
-- 1. 특정 날짜 이전 가장 최근 값은 MAX(date) 서브 쿼리로 추출
-- 2. 조건에 맞는 데이터 없으면 NULL이므로, CASE WHEN 또는 IFNULL로 기본 값(10) 처리
-- 3. 모든 product_id 포함하기 위해 LEFT JOIN 사용