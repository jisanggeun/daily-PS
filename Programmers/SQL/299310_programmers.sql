-- 프로그래머스: 연도별 대장균 크기의 편차 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/299310

SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) OVER (PARTITION BY YEAR(DIFFERENTIATION_DATE)) - SIZE_OF_COLONY AS YEAR_DEV, ID FROM ECOLI_DATA ORDER BY YEAR, YEAR_DEV;

-- 반성
-- 1. YEAR의 data type은 아무 상관 없는 줄 알았는데 int형이였음
-- 2. PARTITION BY로 나눴는데, 다른 날을 고려하지 않아 다른 partition이 되도록 함 (ex. 2019/01/01 and 2019/12/31)
-- 3. 다중 ORDER BY