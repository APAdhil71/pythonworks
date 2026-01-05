def power(a, b):
    if b == 0:
        return 1     #Q9
    return a * power(a, b - 1)
print(power(2, 5))
"""
power(2, 5)
= 2 * power(2, 4)
= 2 * (2 * power(2, 3))
= 2 * (2 * (2 * power(2, 2)))
= 2 * (2 * (2 * (2 * power(2, 1))))
= 2 * (2 * (2 * (2 * (2 * power(2, 0)))))
"""
