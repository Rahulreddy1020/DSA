# Write your MySQL query statement below






with cte as 


(select e.id, e.name as Employee, 

e.salary as Salary, d.name as Department,

Dense_Rank()over(partition by d.name order by e.salary DESC) as rnk


from Employee e

join Department d

on 

e.departmentId = d.id)

select cte.Department, cte.Employee, cte.Salary from cte 

where rnk <=3
