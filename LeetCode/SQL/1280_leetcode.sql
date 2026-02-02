-- LeetCode: Students and Examinations
-- https://leetcode.com/problems/students-and-examinations/?envType=study-plan-v2&envId=top-sql-50

SELECT 
    t1.student_id, t1.student_name, t1.subject_name, COUNT(E.student_id) AS attended_exams 
FROM (
    SELECT * 
    FROM Students S 
    CROSS JOIN Subjects SB 
        GROUP BY S.student_id, SB.subject_name 
        ORDER BY S.student_id, SB.subject_name ASC
    ) t1 
LEFT JOIN Examinations E 
    ON E.student_id = t1.student_id AND E.subject_name = t1.subject_name 
    GROUP BY t1.student_id, t1.subject_name 
    ORDER BY t1.student_id, t1.subject_name;

-- 회고
-- 1. JOIN에 LEFT, RIGHT, INNER, OUTER, SELF만 있는 줄 알았는데 CROSS JOIN이 있다는 걸 알게 됨
-- 2. CROSS JOIN = 모든 조합을 다룸
-- 3. LEFT JOIN이나, RIGHT JOIN과 같은 한쪽 벤다이어 그램만 사용하는 JOIN은 매칭이 안되면 NULL 값이 나오는 걸 항상 인지
-- 4. 따라서, LEFT JOIN이나, RIGHT JOIN 사용 시 SELECT, GROUP BY에서 
-- 4-1. LEFT JOIN의 경우(오른쪽 table column 대신 왼쪽 table column) 사용해야 NULL 방지
-- 4.2. RIGHT JOIN의 경우(왼쪽 table column 대신 오른쪽 table column) 사용해야 NULL 방지