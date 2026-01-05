def sum_n(n):
    if n == 0:      
        return 0 #Q2
    return n + sum_n(n - 1)   
print(sum_n(5))
"""
sum_n(1) = 1
sum_n(2) = 3
sum_n(3) = 6
sum_n(4) = 10
sum_n(5) = 15
"""