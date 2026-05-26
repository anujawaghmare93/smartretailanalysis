-- Total Sales
SELECT SUM(Sales) FROM retail;

-- Top Categories
SELECT Category, SUM(Sales)
FROM retail
GROUP BY Category;

-- Region-wise Profit
SELECT Region, SUM(Profit)
FROM retail
GROUP BY Region;

-- Top Customers
SELECT Customer_Name, SUM(Sales)
FROM retail
GROUP BY Customer_Name
ORDER BY SUM(Sales) DESC
LIMIT 10;