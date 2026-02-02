-- LeetCode: Rising Temperature
-- https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50

SELECT id FROM (SELECT id, DATEDIFF(recordDate, LAG(recordDate) OVER (ORDER BY recordDate)) AS d_diff, temperature - LAG(temperature) OVER (ORDER BY recordDate) AS t_diff FROM Weather) temp_diff WHERE t_diff > 0 and d_diff = 1;

-- 회고
-- 1. LAG를 사용해서 구현, LAG 사용 시 이전 행을 참조하기 때문에 날짜가 2일 이상 차이나도 행끼리 연결되어 있으면 참조됨
-- 2. 따라서, 날짜끼리 연결되어 있는데, 1일 차이나는지 확인
-- 3. 그리고 이전 날에 비해 온도가 올랐는지도 LAG를 통해 확인 
-- 4. FROM 절 안에 서브 쿼리로 작성 (id, recordDate, temperature)

SELECT A_W.id FROM Weather A_W INNER JOIN Weather B_W ON DATEDIFF(A_W.recordDate, B_W.recordDate) = 1 WHERE A_W.temperature > B_W.temperature;

-- 회고
-- 1. 같은 테이블 복사해서 2개로 만든 후 DATEDIFF를 통해, 1일 차이나는 행만 INNER JOIN 진행
-- 2. after weather temperature > before weather temperature 인 경우만 SELECT 