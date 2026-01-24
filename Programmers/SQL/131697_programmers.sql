-- 프로그래머스: 가장 비싼 상품 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/131697

SELECT MAX(PRICE) FROM PRODUCT;
SELECT PRICE FROM PRODUCT ORDER BY PRICE DESC LIMIT 1;