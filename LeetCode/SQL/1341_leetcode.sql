-- LeetCode: Movie Rating
-- https://leetcode.com/problems/movie-rating/?envType=study-plan-v2&envId=top-sql-50

-- 영화 평점 많이 등록한 사용자
SELECT R1.name AS results 
FROM (
    SELECT U.name
    FROM Users U
    INNER JOIN (
        SELECT M1.user_id, COUNT(M1.rating) AS rating_count
        FROM MovieRating M1
            GROUP BY M1.user_id
    ) M2
        ON U.user_id = M2.user_id
        ORDER BY M2.rating_count DESC, U.name ASC 
        LIMIT 1
) R1

UNION ALL

-- 2020년 2월에 평균 평점이 가장 높은 영화
SELECT R2.title 
FROM (
    SELECT M3.title
    FROM (
        SELECT M1.movie_id, AVG(M1.rating) AS rating_avg
        FROM MovieRating M1
            WHERE M1.created_at > "2020-01-31" AND M1.created_at < "2020-03-01"
            GROUP BY M1.movie_id
    ) M2
    INNER JOIN Movies M3
        ON M2.movie_id = M3.movie_id
        ORDER BY M2.rating_avg DESC, M3.title ASC
        LIMIT 1 
) R2

-- 회고
-- 1. 평균 평점 높은 영화 / 평점 많이 등록한 사용자 파트로 나눠서 구현해 UNION 함
-- 1-1. 결과를 세로로 합치려면, UNION 사용, 가로로 합치려면 쉼표 사용 후 FROM절에 나열
-- 2. UNION 내 ORDER BY 및 LIMIT 사용하려면, 서브쿼리로 범위 고려해서 감싸야 함