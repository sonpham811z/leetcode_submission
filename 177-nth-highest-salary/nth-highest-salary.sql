CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    with RankedSalary as(
        select Employee.salary, dense_rank() over (order by Employee.salary desc) as rnk
        from Employee
    ) 
    select max(RankedSalary.salary) from RankedSalary
    where rnk= N
      
  );
END;
$$ LANGUAGE plpgsql;