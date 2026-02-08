-- LeetCode: Friend Requests II: Who Has the Most Friends
-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/?envType=study-plan-v2&envId=top-sql-50

SELECT R.id, COUNT(R.id) AS num
FROM (
    SELECT R1.requester_id as id
    FROM RequestAccepted R1

    UNION ALL 

    SELECT R2.accepter_id as id
    FROM RequestAccepted R2
) R
    GROUP BY R.id
    ORDER BY num DESC
    LIMIT 1

-- 회고
-- 1. requester_id와 accepter_id를 각각 id로 바꾼 후 UNION ALL로 세로로 합침
-- 2. GROUP BY id, COUNT(R.id)로 총 친구 수 계산
-- 3. UNION ALL = 행을 세로로 쌓음 / FULL OUTER JOIN = 컬럼을 가로로 붙임 (다른 개념임 주의 할 것.)

-- 초반에 어렵게 구현했을 때의 코드 (생각 없이 그냥 구현)
SELECT 
    CASE WHEN R5.requester_id IS NOT NULL THEN R5.requester_id ELSE R5.accepter_id END AS id,

    CASE WHEN R5.count_accept IS NOT NULL AND R5.count_request IS NOT NULL 
        THEN R5.count_accept + R5.count_request 
        ELSE CASE WHEN R5.count_accept IS NOT NULL AND R5.count_request IS NULL 
            THEN R5.count_accept 
            ELSE CASE WHEN R5.count_accept IS NULL AND R5.count_request IS NOT NULL 
                THEN R5.count_request
                ELSE 0
                END
            END
        END
    AS num
FROM (
    SELECT *
    FROM (
        SELECT R1.requester_id, COUNT(R1.accepter_id) AS count_accept
        FROM RequestAccepted R1
            GROUP BY R1.requester_id
    ) R3 
    LEFT JOIN (
        SELECT R2.accepter_id, COUNT(R2.requester_id) AS count_request
        FROM RequestAccepted R2
            GROUP BY R2.accepter_id
    ) R4
        ON R3.requester_id = R4.accepter_id

    UNION 

    SELECT *
    FROM (
        SELECT R1.requester_id, COUNT(R1.accepter_id) AS count_accept
        FROM RequestAccepted R1
            GROUP BY R1.requester_id
    ) R3 
    RIGHT JOIN (
        SELECT R2.accepter_id, COUNT(R2.requester_id) AS count_request
        FROM RequestAccepted R2
            GROUP BY R2.accepter_id
    ) R4
        ON R3.requester_id = R4.accepter_id
) R5
    ORDER BY num DESC 
    LIMIT 1