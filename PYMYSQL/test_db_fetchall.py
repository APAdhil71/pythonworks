from mysql import connector
connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="test_db"
)
cursor=connection.cursor()
select_query = "SELECT * FROM users"
cursor.execute(select_query)

result = cursor.fetchall()
for row in result:
    print(row)
cursor.close()
connection.close()


