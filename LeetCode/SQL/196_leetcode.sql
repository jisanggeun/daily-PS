-- LeetCode: Delete Duplicate Emails
-- https://leetcode.com/problems/delete-duplicate-emails/description/?envType=study-plan-v2&envId=top-sql-50

DELETE P1
FROM Person P1
INNER JOIN Person P2
    ON P1.id > P2.id
    AND P1.email = P2.email

-- 회고
-- 1. DELETE FROM 테이블 WHERE 조건 으로 삭제
-- 2. 조건에 맞는 행 전부 삭제됨
-- 3. DELETE문도 JOIN 가능