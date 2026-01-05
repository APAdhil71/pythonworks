def factorial(number):
    if number < 0:
        return 
    fact = 1                   #Q2  factorial
    for i in range(1, number + 1):
        fact= i*fact
    return fact
print(factorial(5))