number = int(input("enter number")) #123

count = 0 #3

while(number!=0): #123!=0 12!=0 #1=0
    digit = number%10 #123%10=3, 12%10=2 1%10=1
    count+=1
    number=number//10 #123//10=12 12//10=1
print(count) #3