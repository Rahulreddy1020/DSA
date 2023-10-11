# Write your MySQL query statement below






WITH CTE AS (
    SELECT 
        query_name,
        rating,
        position,
        CASE WHEN rating < 3 THEN 1 ELSE 0 END as c
    FROM Queries
)

SELECT 
    query_name,
    ROUND(AVG(rating/position),2) as quality,
    ROUND(SUM(c) * 100.0 / COUNT(query_name),2) as poor_query_percentage
FROM 
    CTE
GROUP BY 
    query_name
