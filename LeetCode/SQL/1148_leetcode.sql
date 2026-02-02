-- LeetCode: Article Views I
-- https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=top-sql-50

SELECT DISTINCT author_id AS id FROM Views WHERE author_id = viewer_id ORDER BY id ASC;

-- 회고
-- 1. 자꾸 ORDER BY 할때, column명을 넣는 걸 잊음. 
-- 2. ASC의 경우 default이므로, 사실 안넣어도 되지만 연습용이므로 넣음 (DESC일 경우엔 무조건 넣어야 함)