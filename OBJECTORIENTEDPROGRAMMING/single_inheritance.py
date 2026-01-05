# class Parent:
#     def vehicle (self):
#         print("bmw")
# class Child(Parent):
#     def mobile (self):
#         print("i phone")

# child_instance=Child()
# child_instance.mobile()
# child_instance.vehicle()



"""
single inheritance with constructor
"""
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(f"name={self.name} age={self.age} gender={self.gender}")
class Student(Person):
    roll_number:str
    course:str
    def __init__(self, name, age, gender,roll,course):
        super().__init__(name, age, gender)
        self.roll_number=roll
        self.course=course
    def display(self):
        print(f"roll_number={self.roll_number} course={self.course}")
        super().display()

student_instance=Student("adhil",21,"male",1,"data science")
student_instance.display()