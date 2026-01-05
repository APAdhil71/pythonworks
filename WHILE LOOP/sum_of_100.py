current_number=1
sum_of_evens =0


while(current_number <=100):
    if(current_number%2==0):          #q.4 sum of only even numbers from 1 to 100
        sum_of_evens += current_number
    current_number +=1
print("the sum of even numbers from 1 to 100 is" ,sum_of_evens)