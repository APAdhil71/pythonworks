A={1,2,3,4,5}
B={4,5,6,7,8}
common_elements=A.intersection(B)
print(common_elements)         #Q1 

elements_in_A_only=A.difference(B)
print(elements_in_A_only)

sym_diff=A.symmetric_difference(B)
print(sym_diff)