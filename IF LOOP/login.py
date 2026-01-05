db_password=8888
db_otp =5462

password =int(input("enter the password"))
if db_password==password:
    otp = int(input("enter the otp"))
    if otp ==db_otp:
        print("access granted>>")
    else:
        print("incorrect password")
else:
    print("invalid")
