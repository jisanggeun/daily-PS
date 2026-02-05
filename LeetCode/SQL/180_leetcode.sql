-- LeetCode: Consecutive Numbers
-- https://leetcode.com/problems/consecutive-numbers/description/?envType=study-plan-v2&envId=top-sql-50

SELECT DISTINCT L2.num AS ConsecutiveNums
FROM (
    SELECT L1.id, L1.num, LAG(L1.num, 1) OVER(ORDER BY L1.id) AS bf_num, LEAD(L1.num) OVER(ORDER BY L1.id) AS af_num
    FROM Logs L1
) L2
    WHERE L2.bf_num = L2.num and L2.num = L2.af_num

-- 회고
-- 1. LAG, LEAD 방식으로 풀어봤음 (LAG(컬럼 명, 몇 행 전), LEAD(컬럼 명, 몇 행 후) OVER(ORDER BY 정렬 할 컬럼 명)) 
-- 2. SELF JOIN 방식으로도 가능

SELECT DISTINCT L2.num AS ConsecutiveNums
FROM Logs L1
INNER JOIN Logs L2
INNER JOIN Logs L3
    ON L2.id = L1.id - 1 AND L3.id = L2.id - 1
    WHERE L2.num = L3.num AND L2.num = L1.num