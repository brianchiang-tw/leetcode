SELECT Name AS Customers
From Customers
LEFT JOIN Orders
ON
Customers.Id = Orders.CustomerId
WHERE Orders.CustomerId IS NULL