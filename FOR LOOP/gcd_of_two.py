number1=int(input("enter the number"))
number2=int(input("enter the number"))
gcd=1
small_number =min(number1,number2)
for i in range(1,small_number+1):           #Q4 GCD WITH TWO PARAMETER
    if number1%i==0 and number2%i==0:
        gcd=1
print(gcd)