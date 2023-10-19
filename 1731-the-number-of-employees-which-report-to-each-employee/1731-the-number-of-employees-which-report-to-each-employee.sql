# Write your MySQL query statement below





# select e2.employee_id,e2.name, (count(e1.employee_id)) as reports_count,

# Round(Avg(e1.age),0) as average_age

# from employees e1 
    
#     Inner join
    
#     employees e2
    
#     on 
    
#     e1.reports_to = e2.employee_id
    
#     having c
    
#     group by e2.employee_id
    

    
SELECT
    e.employee_id AS employee_id,
    e.name AS name,
    COUNT(r.employee_id) AS reports_count,
    ROUND(SUM(r.age) / COUNT(r.employee_id)) AS average_age
FROM Employees e
LEFT JOIN Employees r ON e.employee_id = r.reports_to
GROUP BY e.employee_id, e.name
HAVING reports_count > 0
ORDER BY employee_id;

    
    
