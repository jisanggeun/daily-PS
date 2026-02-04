-- LeetCode: Biggest Single Number
-- https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50

SELECT MAX(M.num) AS num
FROM (
    SELECT M1.num, COUNT(M1.num)
    FROM MyNumbers M1
        GROUP BY M1.num
        HAVING COUNT(M1.num) = 1
) M

-- 회고
-- 1. 중복되지 않은 행 중 가장 높은 걸 찾으려면, 
-- 1-1. 중복되지 않은 행만 filtering -> COUNT = 1, (COUNT가 1이므로, 고유 함 증명)
-- 1-2. 그 중 가장 큰 값 찾기 -> 집계 함수 MAX 사용 (가장 큰 값 증명)