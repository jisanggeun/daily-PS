-- LeetCode: User Activity for the Past 30 Days I
-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/?envType=study-plan-v2&envId=top-sql-50

SELECT A.activity_date AS day, COUNT(DISTINCT A.user_id) AS active_users
FROM Activity A
    GROUP BY A.activity_date
    HAVING A.activity_date BETWEEN DATE_ADD("2019-07-27", INTERVAL -29 DAY) AND "2019-07-27"

-- 회고
-- 1. 7월 27일을 포함한 30일이기 때문에 INTERVAL -29일 사용
-- 2. 개선점: 일반 컬럼의 경우 WHERE로 조건 처리 / HAVING의 경우 집계 함수에서 조건 처리 함

-- 개선된 코드
SELECT A.activity_date AS day, COUNT(DISTINCT A.user_id) AS active_users
FROM Activity A
    WHERE A.activity_date BETWEEN DATE_ADD("2019-07-27", INTERVAL -29 DAY) AND "2019-07-27"
    GROUP BY A.activity_date