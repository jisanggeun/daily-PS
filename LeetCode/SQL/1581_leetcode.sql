-- LeetCode: Customer Who Visited but Did Not Make Any Transactions
-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50

SELECT V.customer_id, COUNT(*) as count_no_trans FROM Visits V LEFT JOIN Transactions T ON V.visit_id = T.visit_id WHERE T.transaction_id IS NULL GROUP BY V.customer_id;

-- 회고
-- 1. transaction_id가 NULL인 갯수를 찾는 거기 때문에, LEFT JOIN에 교집합 부분을 제거 (T.transaction_id IS NULL)
-- 2. id 별 transaction_id가 NULL인 갯수이므로, GROUP BY 사용해야 함 (GROUP BY V.customer_id)
-- 3. NULL count를 측정해야 하므로 COUNT(*)을 사용했는데, COUNT(column 명)을 사용할 시 NULL을 제외한 값을 count해서 출력하기 때문