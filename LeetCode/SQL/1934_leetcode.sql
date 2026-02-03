-- LeetCode: Confirmation Rate
-- https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50

SELECT t1.user_id, ROUND(SUM(t1.is_confirmed)/COUNT(t1.is_confirmed), 2) AS confirmation_rate 
FROM (
    SELECT S.user_id, S.time_stamp, C.user_id AS C_user_id, C.time_stamp AS C_time_stamp, C.action, CASE WHEN action = "confirmed" THEN 1 ELSE 0 END AS is_confirmed 
    FROM Signups S 
    LEFT JOIN Confirmations C 
        ON S.user_id = C.user_id

    UNION

    SELECT S.user_id, S.time_stamp, C.user_id AS C_user_id, C.time_stamp AS C_time_stamp, C.action, CASE WHEN action = "confirmed" THEN 1 ELSE 0 END AS is_confirmed 
    FROM Signups S 
    RIGHT JOIN Confirmations C 
        ON S.user_id = C.user_id
) t1 
GROUP BY t1.user_id

-- 회고
-- 1. FULL OUTER JOIN의 경우 MYSQL은 LEFT RIGHT JOIN으로 구현
-- 2. CASE WHEN문 사용해 action이 confirmed일 때만 1로 나머지 상태는 0으로 나오게 설정 (if-else와 동일)
-- 3. table끼리 합칠 때, id가 같으면 나중에 select할 때, 모호해지므로, AS로 이름 바꿔서 예방