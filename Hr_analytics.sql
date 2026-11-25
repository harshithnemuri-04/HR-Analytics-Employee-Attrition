CREATE DATABASE HR_ANALYTICS;
USE HR_ANALYTICS;

CREATE TABLE employees (
    EmployeeNumber INT PRIMARY KEY,
    Age INT,
    Attrition VARCHAR(10),
    BusinessTravel VARCHAR(50),
    Department VARCHAR(100),
    Gender VARCHAR(20),
    JobRole VARCHAR(100),
    MonthlyIncome DECIMAL(10,2),
    OverTime VARCHAR(10),
    JobSatisfaction INT,
    YearsAtCompany INT
); 

USE HR_Analytics;

SHOW TABLES;
select * from employees;

SELECT *
FROM employees
LIMIT 10;

SELECT COUNT(*) AS Total_Employees
FROM employees;
select department,count(*) as Total_Department from employees
group by department;

select attrition,count(*) as employee_count from employees
group by attrition;

SELECT ROUND(AVG(MonthlyIncome), 2)
AS Average_Salary
FROM employees;

select round(sum(case when attrition = 'yes' then 1 else 0 end )*100/count(*),2) as attrition_rate
from employees;

SELECT
Department,
COUNT(*) AS Attrition_Count
FROM employees
WHERE Attrition = 'Yes'
GROUP BY Department;

SELECT
Gender,
COUNT(*) AS Employee_Count
FROM employees
GROUP BY Gender;
 
SELECT
ROUND(AVG(MonthlyIncome), 2) AS Average_Salary
FROM employees;

SELECT
OverTime,
Attrition,
COUNT(*) AS Employee_Count
FROM employees
GROUP BY OverTime, Attrition;

SELECT
JobRole,
COUNT(*) AS Attrition_Count
FROM employees
WHERE Attrition = 'Yes'
GROUP BY JobRole
ORDER BY Attrition_Count DESC;