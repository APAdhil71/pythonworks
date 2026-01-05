class Vehicle:
    def __init__(self,brand,title):
        self.brand=brand
        self.title=title
    def move(self):
        print(self.title,"is moving")
class Car(Vehicle):
    def __init__(self, brand, title):
        super().__init__(brand, title)
class Ship(Vehicle):
    def __init__(self, brand, title):
        super().__init__(brand, title)
    def move(self):
        print(self.title,"is sailing")
car_instance=Car("toyota","fortuner")
ship_instance=Ship("mistu","titanic")
car_instance.move()
ship_instance.move()


"""
✅ What is Overriding in Python?

Overriding happens when a child class (subclass) has a method with the same name as a method in the parent class, and it replaces (overrides) the parent’s method.

Same method name

Same parameters

Defined again in child class

Child method is used instead of parent method
"""
