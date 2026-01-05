from mysql import connector
connection=connector.connect(
    host = "localhost",
    user="root",
    password="Password@123",
    database="test_db"
)
cursor=connection.cursor()
insert_query = """
INSERT INTO users (name, email, age) VALUES (%s, %s, %s)
"""
data = ("Adhil", "adhil@gmail.com", 22)

cursor.execute(insert_query, data)
connection.commit()
print("Data inserted")
