import sqlite3

# Connect to the northwind_small database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Query 1: What are the ten most expensive items
expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""

# Query 2: What is the average age of an employee at the time of their hiring?
avg_hire_age = """
SELECT AVG(HireDate - BirthDate) AS avg_age
FROM Employee;
"""

# Query 3: What are the ten most expensive items?
ten_most_expensive = """
SELECT ProductName, UnitPrice, CompanyName
FROM Product
JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;
"""

# Query 4: What is the largest category (by number of unique products in it)?
largest_category = """
SELECT CategoryName, COUNT(DISTINCT Product.Id) AS num_products
FROM Category
JOIN Product ON Category.Id = Product.CategoryId
GROUP BY Category.Id
ORDER BY num_products DESC
LIMIT 1;
"""

# Close the connection
conn.close()
