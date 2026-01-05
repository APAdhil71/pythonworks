class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    @property
    def get_age(self):
        print(self.age)
    def get_gender(self):
        print(self.gender)
person_instance=Person("adhil",23,"male")
person_instance.get_age
person_instance.get_gender()