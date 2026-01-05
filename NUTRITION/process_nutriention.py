file_path="C:\\Users\\adhil\\OneDrive\\Desktop\\pythonsworks\\NUTRITION\\Food_Nutrition_Dataset.csv.xls"
fr=open(file_path,"r",encoding="utf-8")
import csv
reader=csv.DictReader(fr)
data = [row for row in reader]
high_protein = [row["food_name"] for row in data if float(row["protein"]) > 5]
print("Foods with protein > 5g:", high_protein)
category_count = {}
for row in data:
    cat = row["category"]
    if cat in category_count:
        category_count[cat] += 1
    else:
        category_count[cat] = 1
print(category_count)
vitc_foods =[row["food_name"] for row in data if row["vitamin_c"] and float(row["vitamin_c"]) > 10]
print("vitamin c more than 10:",vitc_foods)
low_fat = [row["food_name"] for row in data if float(row["fat"]) < 2]
print("low fat below 2:",low_fat)
avg = sum(float(row["calories"]) for row in data) / len(data)
print("Average calories =", avg)
print("Total foods =", len(data))
iron_rich = [row["food_name"] for row in data if row["iron"] and float(row["iron"]) > 1]
print(iron_rich)





