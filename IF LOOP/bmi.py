weight_in_kg =int(input("enter weight in kg"))
height_in_cm =int(input("enter height in cm"))
height_in_meter = height_in_cm/100
bmi = weight_in_kg/height_in_meter**2
bmi = round(bmi,0)
print(bmi)
if bmi in range(0,20):
    print("underweight")
elif bmi in range(20,25):
    print ("noraml weight")
elif bmi in range(25,30):
    print ("over weight")
else:
    print ("obese")