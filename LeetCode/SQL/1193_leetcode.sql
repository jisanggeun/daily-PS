-- LeetCode: Monthly Transactions I
-- https://leetcode.com/problems/monthly-transactions-i/description/?envType=study-plan-v2&envId=top-sql-50

SELECT DATE_FORMAT(T.trans_date, "%Y-%m") AS month, T.country, COUNT(T.state) AS trans_count, COUNT(CASE WHEN T.state = "approved" THEN 1 END) AS approved_count, SUM(T.amount) AS trans_total_amount, SUM(CASE WHEN T.state = "approved" THEN T.amount ELSE 0 END) AS approved_total_amount  
FROM Transactions T 
    GROUP BY month, T.country

SELECT DATE_FORMAT(T.trans_date, "%Y-%m") AS month, T.country, COUNT(T.state) AS trans_count, SUM(T.state = "approved") AS approved_count, SUM(T.amount) AS trans_total_amount, SUM(IF(T.state = "approved", T.amount, 0)) AS approved_total_amount  
FROM Transactions T 
    GROUP BY month, T.country   

-- 회고
-- 1. DATE_FORMAT을 통해 Date Format 조건에 맞게 변환 (Y=2026, y=26 / M=December, m=12 / D=18th, d=18)
-- 2. COUNT의 경우 조건을 넣으려면 SUM(조건) 또는 COUNT(CASE WHEN 조건 THEN 1 END)로 해야 함
-- 2-1. SUM(조건)은 boolean이 1/0으로 계산되기 때문
-- 3. SUM의 경우 조건을 넣으려면 SUM(IF(조건, true값, false값)) 또는 SUM(CASE WHEN 조건 THEN true값 ELSE false값 END)로 해야함