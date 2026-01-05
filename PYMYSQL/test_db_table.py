from mysql import connector
connection=connector.connect(
    host = "localhost",
    user="root",
    password="Password@123",
    database="test_db"
)
cursor=connection.cursor()
create_table_query = """
CREATE TABLE  users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT
)
"""

cursor.execute(create_table_query)
connection.commit()
print("Table created successfully")