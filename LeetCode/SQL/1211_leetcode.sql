-- LeetCode: Queries Quality and Percentage
-- https://leetcode.com/problems/queries-quality-and-percentage/description/?envType=study-plan-v2&envId=top-sql-50

SELECT Q.query_name, ROUND(SUM(Q.rating / Q.position) / COUNT(Q.query_name), 2) AS quality, ROUND(SUM(Q.r_count) / COUNT(Q.rating) * 100, 2) AS poor_query_percentage 
FROM (
    SELECT *, CASE WHEN Q1.rating < 3 THEN 1 ELSE 0 END AS r_count
    FROM Queries Q1
) Q
    GROUP BY Q.query_name

-- 회고
-- 1. Aggregate Function을 너무 활용 못해서 코드가 길어짐
-- 2. 개선점: SUM / COUNT 대신 AVG 활용, AVG 함수 내부에 조건을 걸 수 있음

SELECT Q.query_name, ROUND(AVG(Q.rating / Q.position), 2) AS quality, ROUND(AVG(Q.rating < 3) * 100, 2) AS poor_query_percentage
FROM Queries Q
    GROUP BY Q.query_name