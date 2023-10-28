# Write your MySQL query statement below






WITH cte AS (
  SELECT account_id, income, 
    CASE
      WHEN income < 20000 THEN 'Low Salary'
      WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
      WHEN income > 50000 THEN 'High Salary'
    END AS Category
  FROM Accounts
)

SELECT categories.Category, IFNULL(COUNT(cte.account_id), 0) AS accounts_count
FROM (
  SELECT 'Low Salary' AS Category
  UNION ALL
  SELECT 'Average Salary'
  UNION ALL
  SELECT 'High Salary'
) AS categories
LEFT JOIN cte ON categories.Category = cte.Category
GROUP BY categories.Category;
