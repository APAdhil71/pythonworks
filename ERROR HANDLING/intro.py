"""
error handling
1. syntax error
2. logical error
3. run time error (exception) zero divison, value error, key error,file not found



block 
try doubtfull code
except handling code
finally clean up process

keywords
raise
assert
"""
num1=int(input("enter the number1 "))
num2=int(input("enter the number2 "))

try:
    result=num1/num2
    print(result)
except Exception as e:
    print(e)
print("file operation")
print("database commit")