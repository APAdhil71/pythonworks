# def print_numbers(n):
#     if n == 0:
#         return      #Q1
#     print_numbers(n-1)
#     print(n)
# print_numbers(5)




def print_number(n):
    if n==0:
        return 
    print_number(n-1)
    print(n)
print_number(5)