lst=[10,20,30,40,50]
even_b_list=list(map(lambda n:n%2==0,lst))
is_all_even=all(even_b_list)
print(even_b_list)
