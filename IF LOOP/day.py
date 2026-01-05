day=int(input("enter the day"))
if day in range (1,6):
    print("weekday")
elif day in range (6,8):
    print("weekend")
else:
    print("invalid")