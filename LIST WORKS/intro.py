daily_calorie=[1200,1500,1650,1500,3500,1500,1600]
#print(daily_calorie[4])
#daily_calorie[4]=1700
#print(daily_calorie)



"""
print("iteration using index")
for i in range(0,len(daily_calorie)):
    print(daily_calorie[i])
print("object=====")
for d in daily_calorie:
    print(d)
"""

#for d in daily_calorie:
    #if d>1500:
      #  print(d)

total=0
for d in daily_calorie:
    total+=d
print(total)


avg= total//len(daily_calorie)
print(avg)