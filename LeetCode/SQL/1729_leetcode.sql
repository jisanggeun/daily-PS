-- LeetCode: Find Followers Count
-- https://leetcode.com/problems/find-followers-count/description/?envType=study-plan-v2&envId=top-sql-50

SELECT F.user_id, COUNT(F.follower_id) AS followers_count
FROM Followers F
    GROUP BY F.user_id
    ORDER BY F.user_id ASC

-- 회고
-- 1. GROUP BY 사용할 땐 자신 or 집계 함수만 사용