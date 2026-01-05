class Employee:
    id=int
    department=str
    salary=int
    def __init__(self,id,department,salary):
        self.id=id
        self.department=department
        self.salary=salary
    def display(self):
        print(f"id={self.id},department={self.department},salary={self.salary}")
class Developer(Employee):
    programminlang=str
    framework=int
    def __init__(self, id, department, salary,programminglang,framework):
        super().__init__(id, department, salary)
        self.programminlang=programminglang
        self.framework=framework
    def display(self):
        super().display()
        print(f"programming language={self.programminlang},framework={self.framework}")
Employee_instance=Developer(1,"hr",14000,"data science",10)
Employee_instance.display()