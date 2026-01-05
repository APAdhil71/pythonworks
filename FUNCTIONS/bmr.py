def daily_calorie(gender,weight,height,age,activity_level=1.2):
    if gender == "male":
        bmr = 10*weight+6.25*height-5*age+5
    else:
        bmr =10*weight+6.25*height-5*age-161
    return bmr*activity_level
print(daily_calorie("male",62,175,20))


"10* weight (kg)+6.25*height(cm)-5*age(y)+ 5 for man"
# def daily_colorie_consumption(hei,wei,age,gen,act,goal,tagret,duration)
def daily_colorie_consumption(height,weight,age,gender,goal,target,activity_level=1.2,duration=2):
    if gender== "male":
        if goal=="gain" or "loss":
            brm=10*weight+6.25*height-5*age-5
    else:
            brm=10*weight+6.25*height-age-161
            return brm*activity_level*duration
    print(daily_colorie_consumption("male","gain","muscle",62,175,20))