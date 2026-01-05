student={"name":"rahul","age":14,"grade": "B"}
print(student["name"])
student["school"]="city high school"
print(student)
student["grade"]="A"
print(student)         #Q1 DICTIONARY
del student["age"]
print(student)
print("name" in student)
print(len(student))
for key in student:
    print(key)
for value in student.values():
    print(value)
