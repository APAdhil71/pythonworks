class GrandFather:
    def properties(self):
        print("50 cent land 1 huge vintage home")
class Parent(GrandFather):
    def vehicle(self):
        print("swift car")
class Child(Parent):
    def gadgets(self):
        print("iphone,lap")

child_instance=Child()
child_instance.gadgets()
child_instance.properties()
child_instance.vehicle()