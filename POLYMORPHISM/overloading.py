class Calculator:
    def add(self,num1,num2):
        print(num1+num2)
    def add(self,num1,num2,num3): #POLYMORPHISMS
        print(num1+num2+num3)
    def add(self,num1,num2,num3,num4):
        print(num1+num2+num3+num4)
cal_instance=Calculator()
cal_instance.add(100,200)
cal_instance.add(100,200,300,400)

"""
same method name different number of parameters with in a class 
python is not supporting method overrloading
"""