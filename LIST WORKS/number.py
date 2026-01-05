arr=[1,5,7,9,12,15,16,19,20]
print("Even numbers :")
for num in arr:
    if num %2==0:
        print(num)          #Q1 arr 
print("odd numbers:")
for num in arr:
    if num %2!=0:
        print(num)
odd_count=0
for num in arr:
    if num %2!=0:
        odd_count+=1
print("count of odd numbers",odd_count)
even_count=0
for num in arr:
    if num %2==0:
        even_count+=1
print("count of even numbers",even_count)