num1=int(input("enter the number1"))

num2=int(input("enter the number2"))
operation = input("enter the u want to perform + for add - sub*multi for div")
match operation:

    case "+":
        print("addition result",num1+num2)
    case "-":
        print("sub result",num1-num2)
    case "*":
        print("multipli result",num1*num2)
    case "/":
        print("div result",num1/num2)
    case _:
        print("invalid")