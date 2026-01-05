from mysql import connector
connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwise_db"
)
cursor=connection.cursor()
query="""
insert into user(name,email,password)values(%s,%s,%s)
"""
data=[
("dipin","dipin@gmail.com","dipin123"),
("kipin","kipin@gmail.com","kipin123")
]
cursor.executemany(query,data)
connection.commit()
print("query executed...")
cursor.close()
connection.close()