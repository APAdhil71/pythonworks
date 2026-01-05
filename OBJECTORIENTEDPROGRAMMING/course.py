class Course():
    def __init__(self,coursename):
        self.course_name=coursename
    def display(self):
        print(self.course_name)
class Module(Course):
    def __init__(self, coursename,modulename):
        super().__init__(coursename)
        self.module_name=modulename
    def display(self):
        super().display()
        print(self.module_name)
class Lesson(Module):
    def __init__(self, course_name, module_name,lesson_name):
        super().__init__(course_name, module_name)
        self.lesson_name=lesson_name
        print(self.lesson_name)
    def display(self):
        super().display()

class_instance=Lesson("python","OOP","constructor")
class_instance.display()
