num1=int(input("enter the number1 "))
num2=int(input("enter the number2 45"))

try:
    result=num1/num2
    print(result)
except Exception as e:
    num2=int(input("enter the number2"))
    result=num1/num2
    print(result)
finally:
    print("sendng email......")
    print("sending text msg.....")