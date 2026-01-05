num = 1
while(num <= 20):
    if num %3 ==0 and num %5 ==0:
        print("fizzbuzz")
    elif num% 3==0:                #q.2 fizz buzz
        print("fizz")
    elif num %5 ==0:
        print("buzz")
    else:
        print(num)
    num+=1
