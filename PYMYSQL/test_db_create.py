from mysql import connector
connection=connector.connect(
    host = "localhost",
    user="root",
    password="Password@123",
    database="test_db"
)
print("Connected to MySQL")