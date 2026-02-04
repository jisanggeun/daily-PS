-- LeetCode: Classes With at Least 5 Students
-- https://leetcode.com/problems/classes-with-at-least-5-students/description/?envType=study-plan-v2&envId=top-sql-50

SELECT C.class
FROM Courses C
    GROUP BY C.class
    HAVING COUNT(C.student) >= 5;

-- 회고
-- 1. class명으로 GROUPING 후, COUNT(집계 함수) 통해 학생 수 5명 이상인 class만 나오게 설정
-- 2. WHERE은 COUNT가 집계 함수 이므로, 사용 불가 (실행 순서: WHERE -> GROUP BY -> HAVING -> ORDER BY)