-- LeetCode: Immediate Food Delivery II
-- https://leetcode.com/problems/immediate-food-delivery-ii/description/?envType=study-plan-v2&envId=top-sql-50

SELECT ROUND(AVG(R.check_imm) * 100, 2) AS immediate_percentage
FROM (
    SELECT CASE WHEN D.order_date = D.customer_pref_delivery_date THEN 1 ELSE 0 END AS check_imm
    FROM Delivery D 
    INNER JOIN (
        SELECT D1.customer_id, Min(D1.order_date) AS first_order_date
        FROM Delivery D1 
            GROUP BY D1.customer_id 
            ORDER BY first_order_date ASC
    ) D2
    ON D.order_date = D2.first_order_date AND D.customer_id = D2.customer_id
) R

-- 회고
-- 1. 접근 방식: 첫 주문인지 확인하고, order가 imm인지 schedule인지 확인해서 join하는 방식
-- 2. GROUP BY ORDER BY 적용 순서 (GROUP BY 진행 후 -> ORDER BY 진행)
-- 3. ORDER BY 사용 시, SELECT 에서 적용할 대상 제대로 지정해야 함 
-- 4. 반성: ON에서 order_date만 지정하면, 다른 customer_id 중 order_date랑 같은 게 매칭될 수 있으므로, 주의해야 함 
-- 5. SELECT * 사용 시 JOIN된 table에 동일한 컬럼명 있으면 duplicate 컬럼명 에러 발생하므로, 필요한 컬럼명만 작성