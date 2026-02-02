-- LeetCode: Invalid Tweets
-- https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=top-sql-50

SELECT tweet_id FROM Tweets WHERE LENGTH(content) > 15;

-- 회고
-- 1. strictly greater than 의미 == ~ 초과
-- 2. 문자열 길이 == LENGTH