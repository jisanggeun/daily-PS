-- LeetCode: Patients With a Condition
-- https://leetcode.com/problems/patients-with-a-condition/description/?envType=study-plan-v2&envId=top-sql-50

SELECT P1.patient_id, P1.patient_name, P1.conditions
FROM Patients P1
    WHERE P1.conditions LIKE "DIAB1%" 
    OR P1.conditions LIKE "% DIAB1%"

-- 회고
-- 1. 문자열에 특정 문자 포함 확인 방법: LIKE, INSTR, LOCATE
-- 2. LIKE 패턴: % = 아무 문자 0개 이상 의미
    -- 2-1. "DIAB1%" = DIAB1로 시작
    -- 2-2. "%DIAB1" = DIAB1로 마무리
    -- 2-3. "%DIAB1%" = DIAB1 포함
    -- 2-4. "% DIAB1%" = 공백 뒤 DIAB1 포함
-- 3. WHERE 컬럼 LIKE '패턴' 으로 구성
-- 4. INSTR(문자열, 찾을 문자) = 위치 return / 존재 안할 시, 0 return  
-- 5. LOCATE(찾을 문자, 문자열) = 위치 return / 존재 안할 시, 0 return