-- LeetCode: Product Sales Analysis I
-- https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50

SELECT P.product_name, S.year, S.price FROM Sales S INNER JOIN Product P ON P.product_id = S.product_id;

-- 회고
-- 1. table명 옆에 약자 지정할 수 있으니 table명이 길면 약자 사용 고려해보기