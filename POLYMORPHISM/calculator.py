#define a class calculator with add method takes any number of parameter
class Calculator:
    def add(self,*args):
        print(sum(args))
cal_instance=Calculator()
cal_instance.add(100,200,300)