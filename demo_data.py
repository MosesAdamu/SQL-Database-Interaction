import sqlite3

# Open a connection to a new (blank) database file called demo_data.sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Execute CREATE TABLE statement
curs.execute('''
CREATE TABLE demo (
    s TEXT,
    x INTEGER,
    y INTEGER
);
''')

# Write and execute INSERT INTO statements
curs.execute("INSERT INTO demo (s, x, y) VALUES ('g', 3, 9);")
curs.execute("INSERT INTO demo (s, x, y) VALUES ('v', 5, 7);")
curs.execute("INSERT INTO demo (s, x, y) VALUES ('f', 8, 7);")

# Commit changes
conn.commit()

# Queries
# How many rows are in the table?
row_count = curs.execute('SELECT COUNT(*) FROM demo;').fetchall()

# How many rows are there where both x and y are at least 5?
xy_at_least_5 = curs.execute('''
    SELECT COUNT(*)
    FROM demo
    WHERE x >= 5 AND y >= 5;
''').fetchall()

# How many unique values of y are there?
unique_y = curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchall()

# Print the results
print("Row count:", row_count)
print("XY at least 5 count:", xy_at_least_5)
print("Unique Y count:", unique_y)

# Close the connection
conn.close()
