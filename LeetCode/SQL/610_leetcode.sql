-- LeetCode: Triangle Judgement
-- https://leetcode.com/problems/triangle-judgement/description/?envType=study-plan-v2&envId=top-sql-50

SELECT T.x, T.y, T.z, 
    CASE WHEN T.x + T.y > T.z AND T.y + T.z > T.x AND T.x + T.z > T.y THEN "Yes" ELSE "No" END AS triangle
FROM Triangle T

-- 회고
-- 1. 훨씬 간단하게 할 수 있었음 (max < others 대신)
-- 2. 그냥 max값, other값 구할 필요 없이 x + y > z and y + z > x and x + z > y 인 경우는 max와 others를 포함하므로, 성립 

SELECT T4.x, T4.y, T4.z, CASE WHEN T4.max_value < T4.others THEN "Yes" ELSE "No" END AS triangle
FROM (
    SELECT T2.x, T2.y, T2.z, T3.max_value, CASE WHEN T2.x = T3.max_value THEN T2.y + T2.z ELSE CASE WHEN T2.y = T3.max_value THEN T2.x + T2.z ELSE CASE WHEN T2.z = T3.max_value THEN T2.x + T2.y END END END AS others
    FROM Triangle T2
    INNER JOIN (
        SELECT T1.x, T1.y, T1.z, CASE WHEN T1.x > T1.y and T1.x > T1.z THEN T1.x ELSE CASE WHEN T1.y > T1.z THEN T1.y ELSE T1.z END END AS max_value 
        FROM Triangle T1
    ) T3
        ON T2.x = T3.x AND T2.y = T3.y AND T2.z = T3.z
) T4