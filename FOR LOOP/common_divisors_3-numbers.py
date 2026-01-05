num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enetr the number"))

small_number = min(num1,num2,num3)
for i in range (1,small_number+1):
    if num1%i==0 and num2%i==0 and num3%i==0:
        print(1)