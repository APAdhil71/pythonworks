limit=int(input("enter the limit"))
even_sum = 0
for i in range (1,limit+1):
    if i%2==0:
         even_sum= even_sum+1
print(even_sum)