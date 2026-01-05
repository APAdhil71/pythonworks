def count_digits(num):
    if num == 0:            #Q5
        return 0
    return 1 + count_digits(num // 10)
print(count_digits(12345))
""""
count_digits(12345)
= 1 + count_digits(1234)
= 1 + (1 + count_digits(123))
= 1 + (1 + (1 + count_digits(12)))
= 1 + (1 + (1 + (1 + count_digits(1))))
= 1 + (1 + (1 + (1 + (1 + count_digits(0)))))
"""