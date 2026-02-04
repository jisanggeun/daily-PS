-- LeetCode: Number of Unique Subjects Taught by Each Teacher
-- https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description/?envType=study-plan-v2&envId=top-sql-50

SELECT T.teacher_id, COUNT(DISTINCT T.subject_id) AS cnt
FROM Teacher T
    GROUP BY T.teacher_id;

-- 회고
-- 1. GROUP BY를 사용할 때 GROUP BY 특정 컬럼에서 특정 컬럼을 제외한 나머지 컬럼들을 출력할 때 어떤 값이 나올지 모름 -> 따라서, 집계 함수 사용해 출력 
-- (집계 함수 사용 시 값이 하나만 나오기 때문, 따라서 확실한 값임)
-- 2. 거기서 만약 ORDER BY를 사용할 일이 생기면, 집계 함수 또는 alias 기준으로 정렬
-- (아니면 원본 컬럼을 참조하기 때문에, 어떤 값인지 불확실 해짐)