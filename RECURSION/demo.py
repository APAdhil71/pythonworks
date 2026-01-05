"""
Docstring for RECURSION.demo
recursion
a function call itself is called recursion

"""
# def display_hello_world(limit):
#     if limit==0:
#         return
#     print("hello world")
#     return display_hello_world(limit-1)
# display_hello_world(5)


# def display_number(limit):
#     if limit==1:
#         return 1
#     print(limit)
#     return display_number(limit-1)
# display_number(5)

# def display_numbers(limit):
#     if limit==0:
#         return 
#     print(limit)
#     return display_numbers(limit-1)
# display_numbers(15)

# def sum_numbers(limit):
#     if limit==1:
#         return 1
#     return limit+sum_numbers(limit-1)
# print(sum_numbers(5))
"""
sum_of_n(5)
5+sum_numbers(4) = 5 + 10 = 15
4+sum_numbers(3) = 4 + 6 = 10
3+sum_numbers(2) = 3 + 3 = 6
2+sum_numbers(1) = 2 + 1 = 3
"""
# def factorial_numbers(number):
#     if number==1:
#         return 1
#     return number*factorial_numbers(number-1)
# print(factorial_numbers(5))
"""
factorial_numbers(5)
= 5 * factorial_numbers(4) 5*4=20
factorial_numbers(4)
= 4 * factorial_numbers(3) 5*4*3
factorial_numbers(3)
= 3 * factorial_numbers(2) 5*4*3
factorial_numbers(2)
= 2 * factorial_numbers(1) 5*4*3*2
factorial_numbers(1)
= 1   ← base case
"""

# sum_of_digit(number)
# sum_of_digit(543)=> 12

def sum_of_digit(number):
    if number==0:
        return 0
    return number%10+sum_of_digit(number//10)
print(sum_of_digit(234))

"""
sum_of_digit(0) → 0
sum_of_digit(2) → 2 + 0 = 2
sum_of_digit(23) → 3 + 2 = 5
sum_of_digit(234) → 4 + 5 = 9
"""
# product_of_digit(number)

# def product_of_digit(number):
#     if number==0:
#         return 1
#     return number%10*product_of_digit(number//10)
# print(product_of_digit(123))

def reverse_number(number):
    if number ==0:
        return ""
    return str(number%10)+str(reverse_number(number//10))
print(reverse_number(123))