file_path="ERROR HANDLING\\employee salary\\employee_salary_dataset.csv"
fr=open(file_path,"r",encoding="utf-8")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
# for row in data[:5]: #first five rows
#     print(row)
department_count = {}
for row in data:
    dept = row["Department"]
    if dept in department_count:
        department_count[dept] += 1
    else:
        department_count[dept] = 1
# print(department_count)
total = sum(float(row["Monthly_Salary"]) for row in data)
avg = total //len(data)
# print("Average salary:", avg)
high_salary = [row["Name"] for row in data if float(row["Monthly_Salary"]) > 50000]
# print(high_salary)
print("Total employees:", len(data))
result = [row["Name"] for row in data if float(row["Monthly_Salary"]) % 5 == 0] # divisible by 5 
# print(result)
# Find employees NOT in HR
result = [row["Name"] for row in data if row["Department"] != "HR"]
# print(result)



