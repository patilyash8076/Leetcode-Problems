# Write your MySQL query statement below
with temp as(
    SELECT dpt.name as Department, em.name as Employee,salary,
    DENSE_RANK() OVER(PARTITION BY dpt.name ORDER BY salary desc) as sal_rank
    FROM EMPLOYEE em
    INNER JOIN DEPARTMENT dpt ON em.departmentId  = dpt.id
)

select Department, Employee, salary 
FROM temp
WHERE sal_rank <=3
