-- LeetCode: Average Time of Process per Machine
-- https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50

SELECT 
    machine_id, ROUND(SUM(diff_time) / COUNT(process_id), 3) AS processing_time 
FROM (
    SELECT 
        S_A.machine_id, S_A.process_id, E_A.timestamp - S_A.timestamp AS diff_time 
    FROM Activity S_A 
    INNER JOIN Activity E_A 
        ON S_A.process_id = E_A.process_id 
        AND S_A.machine_id = E_A.machine_id 
    WHERE S_A.activity_type = 'start' 
        AND E_A.activity_type = 'end'
) t1 
GROUP BY machine_id;

-- 회고
-- 1. process_id가 0,1만 있는 줄 알고 맨 처음에는 t1, t2해서 inner join 중첩해서 문제를 해결하려 했음
-- 2. process_id가 여러 개 있을 때, 어떻게 해야할 지 몰라 claude랑 상담하면서 풀이 진행 
-- 3. 상황에 맞게 SUM, COUNT와 같은 Aggregate Function을 잘 활용해야겠다라는 생각이 듦.