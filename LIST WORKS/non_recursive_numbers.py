arr=[10,11,12,13,13,13,8,10,9]
non_recursive=[]
for num in arr:
    occ=arr.count(num)
    if occ==1:
        non_recursive.append(num)
print(non_recursive)
