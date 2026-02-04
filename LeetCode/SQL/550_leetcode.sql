-- LeetCode: Game Play Analysis IV
-- https://leetcode.com/problems/game-play-analysis-iv/?envType=study-plan-v2&envId=top-sql-50


SELECT ROUND(COUNT(DISTINCT A2.player_id) / (SELECT COUNT(DISTINCT A4.player_id) FROM Activity A4), 2) AS fraction
FROM Activity A2
INNER JOIN (
    SELECT A1.player_id, MIN(A1.event_date) AS first_login
    FROM Activity A1
        GROUP BY A1.player_id
        ORDER BY first_login ASC
) A3
    ON A3.player_id = A2.player_id AND DATE_ADD(A3.first_login, INTERVAL 1 DAY) = A2.event_date

-- 회고
-- 1. 문제를 잘 읽자. 
-- 1-1. 로그인인데, game play한 거까지 계산했음. 
-- 1-2. 첫 날만 고려하면 되는데, 다른 날도 고려했음.  
-- 2. DATE_ADD 사용 (+1일 계산 위함)
