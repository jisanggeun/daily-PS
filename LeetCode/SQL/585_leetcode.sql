-- LeetCode: Investments in 2016
-- https://leetcode.com/problems/investments-in-2016/?envType=study-plan-v2&envId=top-sql-50

SELECT ROUND(SUM(I2.tiv_2016), 2) AS tiv_2016
FROM (
    SELECT I1.pid, I1.tiv_2016, COUNT(I1.tiv_2015) OVER (PARTITION BY I1.tiv_2015) AS cnt_tiv2015, COUNT(I1.lat) OVER (PARTITION BY I1.lat, I1.lon) AS cnt_pairs
    FROM Insurance I1
) I2
    WHERE I2.cnt_tiv2015 != 1 
    AND I2.cnt_pairs = 1
    
-- 회고
-- 1. 윈도우 함수에서 ORDER BY 없는 경우 파티션 전체 개수, ORDER BY 있으면 현재 행까지 누적 개수 다룸
-- 2. PARTITION BY에 여러 컬럼 넣어 쌍으로 grouping 가능 (ex. PARTITION BY lat, lon)
-- 3. COUNT(컬럼) OVER (PARTITION BY ...)는 key-value 느낌으로 해당 키에 몇 개 행이 있는지 셈