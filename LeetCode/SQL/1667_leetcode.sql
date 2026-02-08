-- LeetCode: Fix Names in a Table
-- https://leetcode.com/problems/fix-names-in-a-table/description/?envType=study-plan-v2&envId=top-sql-50

SELECT U.user_id, CONCAT(UPPER(SUBSTRING(U.name, 1, 1)), LOWER(SUBSTRING(U.name, 2))) AS name
FROM Users U
    ORDER BY U.user_id ASC;

-- 회고
-- 1. MySQL에서 문자열 indexing = name[0] 이런 방식으로는 안됨
-- 2. SUBSTRING으로 문자열 잘라내 CONCAT으로 연결하는 식으로 구성해야 함
-- 2-1. SUBSTRING(문자열, 시작위치, 길이)로 문자열 잘라냄
-- 2-2. CONCAT(SUBSTRING(1번째 문자열), SUBSTRING(2번째 문자열))로 연결
-- 3. 예시) 첫 글자 대문자 + 이후 소문자 = CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2)))