# Write your MySQL query statement below


select p.product_name, s.year, s.price 

from product p 

Inner join sales s on

s.product_id = p.product_id