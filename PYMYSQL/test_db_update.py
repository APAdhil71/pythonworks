from mysql import connector
connection=connector.connect(
    host = "localhost",
    user="root",
    password="Password@123",
    database="test_db"
)
cursor=connection.cursor()
update_query=update_query = """
UPDATE users SET age = %s WHERE email = %s
"""

cursor.execute(update_query, (23, "adhil@gmail.com"))
connection.commit()
print("Data updated")
