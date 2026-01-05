arr=[10,11,12,13,13,13,8,10,9]

recursive_numbers=[]
for num in arr:
    occ=arr.count(num)
    if occ>1 and num not in recursive_numbers:
        recursive_numbers.append(num)
print(recursive_numbers) 
