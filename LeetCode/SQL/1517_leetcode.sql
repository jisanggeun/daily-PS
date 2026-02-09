-- LeetCode: Find Users With Valid E-Mails
-- https://leetcode.com/problems/find-users-with-valid-e-mails/submissions/1912957097/?envType=study-plan-v2&envId=top-sql-50

SELECT U.user_id, U.name, U.mail
FROM Users U
    WHERE REGEXP_LIKE(U.mail, "^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$", "c")

-- 회고
-- 1. REGEXP = 정규표현식 매칭 연산자
-- 2. [] 안에서 -는 범위를 의미 / 문자로 사용하려면 맨 처음이나 맨 끝에 위치해야 함
-- 3. . = 정규식에서 아무 문자를 의미하므로, 진짜 점을 사용하려면 \\.로 해야 함 
-- 4. REGEXP는 기본적으로 대소문자 구분을 하지 않음
-- 4-1. 따라서, 대소문자를 구분하려면 REGEXP_LIKE(컬럼, 패턴, "c") 사용 