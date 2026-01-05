def my_vehicle(vehicle_name):
    print("my favorite vehicle name is",vehicle_name)
#my_vehicle("bmw")





#even or odd


def number_check(number):
    if number%2==0:
        return "even"
    else:
        return "odd"
#print(number_check(16))




#is positive

def is_poistive(number):
    if number>0:
        return True
    else:
        return False
#print(is_poistive(-19))

def is_negetive(number):
    if number<0:
        return True
    else:
        return False
#print(is_negetive(-17))

def max_two(num1,num2):
    if num1>=num2:
        return num1
    else:
        return num2
#print(max_two(17,14))

def min_two(num1,num2):
    if num1<=num2:
        return num2
    else:
        return num2
#print(min_two(17,10))



def is_leapyear(year):
    if (year%100==0 or year%400==0) or (year%100!=0 and year%4==0):
        return True
    else:
        return False
#print(is_leapyear(2000))
#print(is_leapyear(1999))

def bmi (height_in_cm,weight_in_kg):
    height_in_meter=height_in_cm/100
    result = weight_in_kg/(height_in_meter**2)
    return round(result)
#print(bmi(180,62))


    


