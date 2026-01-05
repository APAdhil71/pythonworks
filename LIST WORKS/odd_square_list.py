odd_square_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
square=[]
for n in odd_square_list:
    if n % 2 !=0:    #Q7
        sq=n*n
        square.append(sq)
print(square)