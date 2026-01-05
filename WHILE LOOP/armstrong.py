number=int(input("enter the number"))
number_copy=number
count=0
sum=0
while(number!=0):
    digit = number%10
    count+=1
    number=number//10
while(number_copy!=0):
    digit = number_copy%10
    expo=digit**count
    sum=sum+expo
    number_copy=number_copy//10
print(sum)