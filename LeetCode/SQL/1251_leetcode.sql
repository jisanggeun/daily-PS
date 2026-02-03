-- LeetCode: Average Selling Price
-- https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50

SELECT P.product_id, CASE WHEN U.purchase_date IS NULL THEN 0 ELSE ROUND(SUM(P.price * U.units) / SUM(U.units), 2) END AS average_price
FROM Prices P 
LEFT JOIN UnitsSold U 
    ON P.product_id = U.product_id 
    WHERE (TIMEDIFF(P.start_date, U.purchase_date) <= 0 AND TIMEDIFF(P.end_date, U.purchase_date) >= 0) OR U.purchase_date IS NULL
    GROUP BY P.product_id

-- 회고
-- 1. JOIN 어떤거 사용할 지 생각 잘 하기
-- 2. CASE WHEN 조건 THEN (True시 값) ELSE (False 시 값) END AS 새로 추가할 항 이름으로 구성
-- 3. 개선점: WHERE에 TIMEDIFF 써서 날짜(purchase_date) 조건 계산하는거도 가능하지만 그냥 AND 써서 구현할 수 있음 이게 더 간단할 듯함

SELECT P.product_id, CASE WHEN U.purchase_date IS NULL THEN 0 ELSE ROUND(SUM(P.price * U.units) / SUM(U.units), 2) END AS average_price
FROM Prices P 
LEFT JOIN UnitsSold U 
    ON P.product_id = U.product_id 
    WHERE U.purchase_date BETWEEN P.start_date AND P.end_date OR U.purchase_date IS NULL
    GROUP BY P.product_id

-- 이게 가장 깔끔한 답
SELECT P.product_id, CASE WHEN U.purchase_date IS NULL THEN 0 ELSE ROUND(SUM(P.price * U.units) / SUM(U.units), 2) END AS average_price
FROM Prices P
LEFT JOIN UnitsSold U
    ON P.product_id = U.product_id
    AND U.purchase_date BETWEEN P.start_date AND P.end_date
    GROUP BY P.product_id

-- 3-1. WHERE절 사용할 때는 TIMEDIFF 조건을 넣으면 매칭 안 된 행(NULL)이 필터링되어서 UnitsSold table에 아예 값이 없을 때의 케이스 오답 발생
-- 따라서, U.purchase_date가 값이 없을 때를 대비한 IS NULL을 통해 빈 값도 받도록 조건 조정
-- 3-2. 또는, ON절에 BETWEEN AND로 교체하면, LEFT JOIN이므로, null 값은 자동으로 받고, CASE문에 의해 자동으로 0으로 set됨


