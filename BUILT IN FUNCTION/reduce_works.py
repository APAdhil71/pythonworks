from functools import reduce
lst=[10,20,30,40,50]
min_num=reduce(lambda n1,n2 : n1 if n1<n2 else n1,lst)
print(min_num)
max_num=reduce(lambda n1,n2 : n1 if n1>n2 else n2,lst)
print(max_num)
product=reduce(lambda n1,n2 : n1*n2,lst)
print(product)