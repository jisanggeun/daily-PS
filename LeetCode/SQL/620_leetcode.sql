-- LeetCode: Not Boring Movies
-- https://leetcode.com/problems/not-boring-movies/?envType=study-plan-v2&envId=top-sql-50

SELECT * FROM Cinema C WHERE C.description != "boring" and C.id % 2 = 1 ORDER BY C.rating DESC

-- 회고
-- 1. alias 활용 습관 들이느라 사용
-- 2. 홀수 짝수 구분할때 %로 구분